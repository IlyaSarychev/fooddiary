from django.db import models
from django.contrib.auth.models import User


class Day(models.Model):
    '''День в дневнике'''

    user = models.ForeignKey(User, null=True, blank=True, related_name='days', on_delete=models.CASCADE)
    date = models.DateField('Дата', auto_now_add=True)

    class Meta:
        ordering = ('-date',)