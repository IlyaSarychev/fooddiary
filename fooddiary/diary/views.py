from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from .models import Day


class DaysListView(ListView):
    '''список дней в дневнике'''

    template_name = 'diary/days/list.html'
    context_object_name = 'days_list'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Day.objects.filter(user=self.request.user)
        else:
            return Day.objects.filter(id__in=self.request.session.get('days', []))


@require_POST
def add_day(request):
    '''Добавление дня в дневник'''

    if request.user.is_authenticated:
        Day.objects.get_or_create(user=request.user, date=request.POST.get('day_date'))
    else:
        day = Day.objects.get_or_create(date=request.POST.get('day_date'))[0]
        if request.session.get('days', False):
            request.session['days'].append(day.id)
        else:
            request.session['days'] = [day.id]

    return HttpResponseRedirect(reverse('days_list'))