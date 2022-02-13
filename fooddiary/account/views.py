from django.http import JsonResponse
from django.shortcuts import render


def ajax_close_login_recommendation_view(request):
    '''Обработка ajax запроса на закрытие уведомления'''

    request.session['login_recommendation_closed'] = True
    return JsonResponse({'success': True})