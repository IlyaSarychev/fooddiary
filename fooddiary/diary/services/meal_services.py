from ..forms import MealForm
from ..models import Day, MealFood, Food, Meal


def create_meal_from_request(request):
    '''Создать прием пищи из POST-запроса'''

    form = MealForm(request.POST)
    meal = form.save(commit=False)
    meal.day = Day.objects.get(id=request.POST.get('day'))

    if request.user.is_authenticated:
        meal.user = request.user
    else:
        meal.session_key = request.session.session_key

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


def add_food_to_meal(request, meal_id):
    '''Добавить связь еды и приема пищи'''

    food = Food.objects.get(id=request.POST.get('food'))
    grams = request.POST.get('grams')

    print(request.session.session_key)

    if request.user.is_authenticated:
        meal = Meal.objects.get(id=meal_id, user=request.user)
    else:
        meal = Meal.objects.get(id=meal_id, session_key=request.session.session_key)

    return MealFood.objects.create(
        food=food,
        meal=meal,
        grams=grams
    )