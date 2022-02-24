class SessionSavingMiddleware:
    '''
    Сохранение сессии для каждого запроса неавторизованного пользователя.
    Если не сохранять сессию, то session_key нужный для логики приложения иногда будет None
    '''

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if not request.user.is_authenticated and not request.session.session_key:
            request.session.save()
