from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView

from .services import registration_services, profile_services
from .forms import ProfileLoginForm, NewUserForm, ChangeProfileInfoForm
from .models import Profile


def ajax_close_login_recommendation_view(request):
    '''Обработка ajax запроса на закрытие уведомления'''

    request.session['login_recommendation_closed'] = True
    return JsonResponse({'success': True})


class ProfileLoginView(LoginView):
    '''Страница входа'''

    form_class = ProfileLoginForm


def user_registration_view(request):
    '''Регистрация нового пользователя'''

    if request.method == 'GET':
        form = NewUserForm()
        return render(request, 'registration/sign_up.html', {'form': form})
    else:
        form = NewUserForm(request.POST)
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
        kwargs['profile_edit_form'] = ChangeProfileInfoForm(instance=self.get_object())
        return kwargs


def edit_profile_view(request):
    '''Обработка формы изменения данных профиля пользователя'''

    profile_services.change_profile_info(request)
    return HttpResponseRedirect(reverse('profile'))