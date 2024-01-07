from django.shortcuts import render, redirect, get_object_or_404
from main import models, forms

HTML_TEMPLATE = 'main/main_page/coaches.html'


def get_coaches(request):
    return render(request, HTML_TEMPLATE, {'coaches': get_grouped_coaches(request),
                                           'form_coach_add': forms.CoachAddForm()})


def add_coach(request):
    if request.method == 'POST':
        form_coach_add = forms.CoachAddForm(request.POST, request.FILES)
        if form_coach_add.is_valid():
            form_coach_add.save()
    return redirect('/coaches')


def update_coach(request, coach_id):
    if request.method == 'POST':
        form_coach_update = forms.CoachUpdateForm(request.POST, request.FILES,
                                                  instance=models.CoachProfile.objects.get(id=coach_id))
        if form_coach_update.is_valid():
            form_coach_update.save()
    return redirect('/coaches')


def delete_coach(request, coach_id):
    if request.method == 'POST':
        get_object_or_404(models.CoachProfile, pk=coach_id).delete()
    return redirect('/coaches')


def get_grouped_coaches(request):
    coaches = []
    for coach in models.CoachProfile.objects.all():
        coach_dict = coach.__dict__
        coach_dict['name'] = f'{coach.user.user.first_name} {coach.user.user.last_name}'
        coach_dict['image'] = coach.image
        coach_dict['form_coach_update'] = forms.CoachUpdateForm(instance=coach)
        for cls in models.Class.objects.all():
            if str(coach) in [str(user) for user in cls.users.all()]:
                coach_dict.setdefault('classes', []).append(f'{cls.offer.category} lessons')
        coach_dict['classes'] = set(coach_dict['classes'])
        coaches.append(coach_dict)
    return coaches
