from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Day(models.Model):
    '''День в дневнике'''

    user = models.ForeignKey(User, null=True, blank=True, related_name='days', on_delete=models.CASCADE)
    date = models.DateField('Дата')
    session_key = models.CharField('Ключ сессии', max_length=40, null=True, blank=True)

    class Meta:
        ordering = ('-date',)


class Meal(models.Model):
    '''Прием пищи'''

    user = models.ForeignKey(User, null=True, blank=True, related_name='meals', on_delete=models.CASCADE)
    session_key = models.CharField('Ключ сессии', max_length=40, null=True, blank=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE, related_name='meals')
    time = models.TimeField('Время приема пищи', default=timezone.localtime)
    food = models.ManyToManyField('Food', verbose_name='Еда', through='MealFood')
    calories = models.PositiveIntegerField('Калорий всего', default=0)

    class Meta:
        ordering = ('day', 'time')


class Food(models.Model):
    '''Еда'''

    user = models.ForeignKey(User, null=True, blank=True, related_name='food', on_delete=models.CASCADE)
    session_key = models.CharField('Ключ сессии', max_length=40, null=True, blank=True)
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание', null=True, blank=True)
    calories = models.PositiveIntegerField('Калорийность на 100г')
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    meals = models.ManyToManyField('Meal', related_name='meals', through='MealFood')

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title


class MealFood(models.Model):
    '''Связь m2m приемов пищи и еды'''
    
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal_food')
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='meal_food')
    grams = models.PositiveIntegerField('Количество грамм')
    date = models.DateTimeField('Дата добавления', auto_now_add=True)