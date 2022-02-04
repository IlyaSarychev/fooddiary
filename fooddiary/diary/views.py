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
            return Day.objects.filter(session_key=self.request.session.session_key)


@require_POST
def add_day(request):
    '''Добавление дня в дневник'''

    post_date = request.POST.get('day_date')

    if request.user.is_authenticated:
        Day.objects.get_or_create(user=request.user, date=post_date)
    else:
        Day.objects.get_or_create(session_key=request.session.session_key, date=post_date)

    return HttpResponseRedirect(reverse('days_list'))