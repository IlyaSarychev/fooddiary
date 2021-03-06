# Generated by Django 4.0.2 on 2022-02-07 07:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0009_alter_meal_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='meals',
            field=models.ManyToManyField(related_name='foods', through='diary.MealFood', to='diary.Meal'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='food',
            field=models.ManyToManyField(related_name='meal', through='diary.MealFood', to='diary.Food', verbose_name='Еда'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='time',
            field=models.TimeField(default=django.utils.timezone.localtime, verbose_name='Время приема пищи'),
        ),
        migrations.AlterField(
            model_name='mealfood',
            name='grams',
            field=models.PositiveIntegerField(verbose_name='Количество грамм'),
        ),
    ]
