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

    post_date = request.POST.get('day_date')

    if request.user.is_authenticated:
        Day.objects.get_or_create(user=request.user, date=post_date)
    else:
        users_days = request.session.get('days', False)
        if users_days:
            if not Day.objects.filter(id__in=users_days, date=post_date).exists():
                request.session['days'].append(Day.objects.create(date=post_date).id)
                request.session.modified = True
        else:
            request.session['days'] = [Day.objects.create(date=post_date).id]

    return HttpResponseRedirect(reverse('days_list'))