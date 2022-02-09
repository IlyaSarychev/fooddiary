from django import forms
from .models import Food, Meal


class CreateFoodForm(forms.ModelForm):
    '''Форма создания и изменения еды'''

    class Meta:
        model = Food
        fields = ['title', 'description', 'calories']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for bfield in self.visible_fields():
            bfield.field.widget.attrs['class'] = 'form-control'

            if bfield.field.widget.__class__.__name__ == 'Textarea':
                bfield.field.widget.attrs['rows'] = '3'


class MealForm(forms.ModelForm):
    '''Форма создания и изменения приемов пищи'''

    class Meta:
        model = Meal
        fields = ['time']

    food = forms.ModelChoiceField(
        queryset=Food.objects.none(),
        label='Еда',
        empty_label='Выберите еду'
    )

    grams = forms.IntegerField(
        min_value=0,
        label='Граммов',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Кол-во граммов'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        # Установить поле request переданное из view.
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)

        # Вывод данных поля в соответствии с аутентификацией пользователя
        if self.request.user.is_authenticated:
            self.fields['food'].queryset = Food.objects.filter(user=self.request.user)
        else:
            self.fields['food'].queryset = Food.objects.filter(session_key=self.request.session.session_key)

        # Добавить bootstrap классы
        for bfield in self.visible_fields():
            if bfield.field.label == 'Еда':
                bfield.field.widget.attrs['class'] = 'form-select'
            else:
                bfield.field.widget.attrs['class'] = 'form-control'