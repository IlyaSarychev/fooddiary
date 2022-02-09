from ..forms import MealForm
from ..models import Day, MealFood, Food


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
    
    food_id_values = [request.POST.get(key) for key in request.POST if key.startswith('food')]
    grams_values = [request.POST.get(key) for key in request.POST if key.startswith('grams')]
    for (food_id, grams) in zip(food_id_values, grams_values):
        MealFood.objects.create(
            meal=meal,
            food=Food.objects.get(id=food_id),
            grams=grams
        )

    return meal