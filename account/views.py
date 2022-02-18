from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView

from .services import registration_services, profile_services, calculator_services
from . import forms
from .models import Profile


def ajax_close_login_recommendation_view(request):
    '''Обработка ajax запроса на закрытие уведомления'''

    request.session['login_recommendation_closed'] = True
    return JsonResponse({'success': True})


class ProfileLoginView(LoginView):
    '''Страница входа'''

    form_class = forms.ProfileLoginForm


def user_registration_view(request):
    '''Регистрация нового пользователя'''

    if request.method == 'GET':
        form = forms.NewUserForm()
        return render(request, 'registration/sign_up.html', {'form': form})
    else:
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            registration_services.set_current_models_user_fields(request, new_user)
            Profile.objects.create(user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse('days_list'))
        else:
            return render(request, 'registration/sign_up.html', {'form': form})


class ProfileDetailView(DetailView):
    '''Профиль пользователя'''

    template_name = 'profile/detail.html'
    
    def get_object(self):
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        '''Добавить дополнительный контекст динамически'''
        kwargs = super().get_context_data(**kwargs)
        # Форма изменения данных профиля
        kwargs['profile_edit_form'] = forms.ChangeProfileInfoForm(instance=self.get_object())
        return kwargs


def edit_profile_view(request):
    '''Обработка формы изменения данных профиля пользователя'''

    profile_services.change_profile_info(request)
    return HttpResponseRedirect(reverse('profile'))


def calorie_consumption_calculator_view(request):
    '''Страница расчета расхода калорий пользователя'''

    profile = request.user.profile

    if request.method == 'POST':
        form = forms.ProfileCalorieConsumptionForm(request.POST)
        if form.is_valid():
            calorie_consumption = calculator_services.calculate_calorie_consumption(
                sex=request.POST.get('sex'),
                weight=int(request.POST.get('weight')),
                height=int(request.POST.get('height')),
                age=int(request.POST.get('age')),
                activity=float(request.POST.get('activity'))
            )
            profile.calorie_consumption = calorie_consumption
            profile.save()
            
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = forms.ProfileCalorieConsumptionForm(instance=profile)
        
    return render(request, 'calculator/detail.html', {
        'form': form
    })