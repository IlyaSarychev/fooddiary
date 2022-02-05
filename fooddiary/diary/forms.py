import imp
from django import forms
from .models import Food


class CreateFoodForm(forms.ModelForm):
    '''Форма создания еды'''

    class Meta:
        model = Food
        fields = ['title', 'description', 'calories']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for bfield in self.visible_fields():
            bfield.field.widget.attrs['class'] = 'form-control'

            if bfield.field.widget.__class__.__name__ == 'Textarea':
                bfield.field.widget.attrs['rows'] = '3'