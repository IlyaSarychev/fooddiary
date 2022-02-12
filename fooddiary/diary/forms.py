from django import forms
from .models import Food, Meal, MealFood


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
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Добавить bootstrap классы
        for bfield in self.visible_fields():
            if bfield.field.label == 'Еда':
                bfield.field.widget.attrs['class'] = 'form-select'
            else:
                bfield.field.widget.attrs['class'] = 'form-control'


class MealFoodForm(forms.ModelForm):
    '''Форма создания связей приемов пищи и еды'''

    class Meta:
        model = MealFood
        fields = ['grams']

    food = forms.ModelChoiceField(
        queryset=Food.objects.none(),
        empty_label='Выбрать еду',
        label='Еда'
    )

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if request:
            self.request = request

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