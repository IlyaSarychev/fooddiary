from diary.models import Day, Meal, Food


def set_current_models_user_fields(request, user):
    '''Установить значение поля user объектов, привязанных к сессии. 
    (Делает пользователя владельцем привязанных к сессии еды, дней, приемов пищи и др.)'''

    Day.objects.filter(session_key=request.session.session_key).update(user=user)
    Meal.objects.filter(session_key=request.session.session_key).update(user=user)
    Food.objects.filter(session_key=request.session.session_key).update(user=user)