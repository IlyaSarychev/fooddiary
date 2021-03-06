from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User

from account.models import Profile


class ProfileLoginForm(auth_forms.AuthenticationForm):
    '''Измененная форма входа в аккаунт'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Добавить bootstrap классы
        for bfield in self.visible_fields():

            field = bfield.field

            if field.label == 'Еда':
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

            # добавить bs классы валидации
            if len(bfield.errors):
                field.widget.attrs['class'] = field.widget.attrs['class'] + ' is-invalid'


class NewUserForm(auth_forms.UserCreationForm):
    '''Форма создания пользователя'''

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        return user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Добавить bootstrap классы
        for bfield in self.visible_fields():

            field = bfield.field

            if field.label == 'Еда':
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

            # добавить bs классы валидации
            if len(bfield.errors):
                field.widget.attrs['class'] = field.widget.attrs['class'] + ' is-invalid'



class ChangeProfileInfoForm(forms.ModelForm):
    '''Форма изменения данных профиля'''

    SEX_CHOICES = [
        (None, 'Выберите пол'),
        ('male', 'Мужской'),
        ('female', 'Женский')
    ]

    sex = forms.ChoiceField(
        choices=SEX_CHOICES,
        label='Пол'
    )

    class Meta:
        model = Profile
        fields = ('sex', 'weight', 'height', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Добавить bootstrap классы
        for bfield in self.visible_fields():

            field = bfield.field

            if field.widget.__class__.__name__ in ('Select'):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProfileCalorieConsumptionForm(ChangeProfileInfoForm, forms.ModelForm):
    '''Форма модели Profile для рассчета суточного расхода калорий'''

    ACTIVITY_CHOICES = [
        (None, 'Ваш уровень активности'),
        (1.2, 'Практически отсутствует'),
        (1.375, 'До 3-х раз в неделю'),
        (1.55, '3-5 раз в неделю'),
        (1.725, '6-7 раз в неделю'),
        (1.9, 'hard mode'),
    ]

    activity = forms.ChoiceField(
        choices=ACTIVITY_CHOICES,
        label='Уровень активности'
    )