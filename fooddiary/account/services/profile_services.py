from ..forms import ChangeProfileInfoForm


def change_profile_info(request):
    '''Изменить данные профиля'''

    profile = request.user.profile
    form = ChangeProfileInfoForm(request.POST)

    if form.is_valid():
        profile.sex = request.POST.get('sex') if request.POST.get('sex') else None
        profile.weight = request.POST.get('weight') if request.POST.get('weight') else None
        profile.height = request.POST.get('height') if request.POST.get('height') else None
        profile.age = request.POST.get('age') if request.POST.get('age') else None
        profile.save()