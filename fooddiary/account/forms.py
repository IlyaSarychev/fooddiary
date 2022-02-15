from django import forms
from django.contrib.auth import forms as auth_forms
from django.contrib.auth.models import User


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