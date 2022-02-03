from django.views.generic import ListView


class DaysListView(ListView):
    '''список дней в дневнике'''

    template_name = 'diary/days/list.html'

    def get_queryset(self):
        return ''