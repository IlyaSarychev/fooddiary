from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from django.views.decorators.http import require_POST
from .models import Day, Food


class DaysListView(ListView):
    '''Список дней в дневнике'''

    template_name = 'diary/days/list.html'
    context_object_name = 'days_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Day.objects.filter(user=self.request.user)
        else:
            return Day.objects.filter(session_key=self.request.session.session_key)


@require_POST
def add_day(request):
    '''Добавление дня в дневник'''

    post_date = request.POST.get('day_date')

    if request.user.is_authenticated:
        Day.objects.get_or_create(user=request.user, date=post_date)
    else:
        Day.objects.get_or_create(session_key=request.session.session_key, date=post_date)

    return HttpResponseRedirect(reverse('days_list'))


class DayDetailView(DetailView):
    '''Страница одного дня'''

    template_name = 'diary/days/detail.html'

    def get_object(self):
        return Day.objects.get(id=self.kwargs['id'])


class MyFoodListView(ListView):
    '''Список еды пользователя'''

    template_name = 'diary/food/list.html'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Food.objects.filter(user=self.request.user)
        else:
            return Food.objects.filter(session_key=self.request.session.session_key)


class MyFoodCreateView(CreateView):
    '''Добавление еды пользователем'''

    pass