from django.db import models


class Profile(models.Model):
    '''Профиль пользователя'''

    user = models.ForeignKey('auth.user', on_delete=models.CASCADE, related_name='profile')
    registered = models.DateTimeField('Дата регистрации', auto_now_add=True)
    sex = models.CharField('Пол', null=True, blank=True, max_length=7)
    weight = models.PositiveSmallIntegerField('Вес', null=True, blank=True)
    height = models.PositiveSmallIntegerField('Рост (в см.)', null=True, blank=True)
    age = models.PositiveSmallIntegerField('Возраст', null=True, blank=True)