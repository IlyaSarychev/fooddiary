from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.decorators.http import require_POST
from .models import Day, Food
from .forms import CreateFoodForm, MealForm
from .services import meal_services


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

    def get_context_data(self, **kwargs):
        '''Добавить форму с переданным request'''
        kwargs = super().get_context_data(**kwargs)
        kwargs['form'] = MealForm(request=self.request)
        return kwargs


class MyFoodListView(ListView):
    '''Список еды пользователя'''

    template_name = 'diary/food/list.html'
    context_object_name = 'food'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Food.objects.filter(user=self.request.user)
        else:
            return Food.objects.filter(session_key=self.request.session.session_key)


class MyFoodCreateView(CreateView):
    '''Добавление еды пользователем'''

    template_name = 'diary/food/create.html'
    form_class = CreateFoodForm
    success_url = reverse_lazy('my_food_list')

    def form_valid(self, form):
        food = form.save(commit=False)
        if self.request.user.is_authenticated:
            food.user = self.request.user
        else:
            food.session_key = self.request.session.session_key
        food.save()
        return HttpResponseRedirect(self.success_url)
    

def delete_my_food_view(request, id):
    '''Удаление еды пользователя по id'''

    if request.user.is_authenticated:
        Food.objects.get(user=request.user, id=id).delete()
    else:
        Food.objects.get(session_key=request.session.session_key, id=id).delete()

    return HttpResponseRedirect(reverse('my_food_list'))


class MyFoodUpdateView(UpdateView):
    '''Изменение еды пользователя'''

    model = Food
    template_name = 'diary/food/update.html'
    form_class = CreateFoodForm
    success_url = reverse_lazy('my_food_list')


@require_POST
def create_meal_view(request):
    '''Создать прием пищи'''

    meal_services.create_meal_from_request(request)
    return HttpResponseRedirect(reverse('day_detail', args=[request.POST.get('day')]))