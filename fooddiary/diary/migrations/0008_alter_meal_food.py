# Generated by Django 4.0.2 on 2022-02-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0007_alter_food_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='food',
            field=models.ManyToManyField(related_name='food', through='diary.MealFood', to='diary.Food', verbose_name='Еда'),
        ),
    ]