from django import template


register = template.Library()

def getattribute(value, arg):
    """Получить атрибут"""

    return value[arg]


register.filter('getattribute', getattribute)