from ..forms import MealForm
from ..models import Day, MealFood, Food, Meal


def create_meal_from_request(request):
    '''Создать прием пищи из POST-запроса'''

    form = MealForm(request.POST, request=request)
    meal = form.save(commit=False)
    meal.day = Day.objects.get(id=request.POST.get('day'))

    # установка значения поля пользователя или ключа сессии
    if request.user.is_authenticated:
        meal.user = request.user
    else:
        if not request.session.session_key:
            request.session.create()
        meal.session_key = request.session.session_key

    meal.save()
    
    total_calories = 0
    food_id_values = [request.POST.get(key) for key in request.POST if key.startswith('food')]
    grams_values = [request.POST.get(key) for key in request.POST if key.startswith('grams')]
    for (food_id, grams) in zip(food_id_values, grams_values):
        food = Food.objects.get(id=food_id)
        MealFood.objects.create(
            meal=meal,
            food=food,
            grams=grams
        )
        total_calories += int(food.calories / 100 * int(grams)) 

    meal.calories = total_calories
    meal.save()

    return meal


def delete_meal_by_id(request, meal_id):
    '''Удалить прием пищи по id у пользователя'''

    if request.user.is_authenticated:
        deleted = Meal.objects.filter(user=request.user, id=meal_id).delete()
    else:
        deleted = Meal.objects.filter(session_key=request.session.session_key, id=meal_id).delete()

    return deleted


def get_meal_info(meal_id):
    '''Получить информацию о приеме пищи (еда, граммы, калории)'''

    meal = Meal.objects.get(id=meal_id)
    data = []

    for meal_food in meal.meal_food.all():
        item = {
            'grams': meal_food.grams
        }
        item['food_title'] = meal_food.food.title
        item['food_calories'] = meal_food.food.calories
        item['calories'] = int(meal_food.grams * (meal_food.food.calories / 100))
        data.append(item)

    return data