from django.shortcuts import render, redirect, get_object_or_404
from main import models, forms

HTML_TEMPLATE = 'main/main_page/activities.html'


def get_activities(request):
    return render(request, HTML_TEMPLATE,
                  {'activities': get_grouped_activities(request),
                   'form_activity_add': forms.EventAddForm() if is_event(request) else forms.ActivityAddForm()})


def add_activity(request):
    if request.method == 'POST':
        form_activity_add = forms.EventAddForm(request.POST, request.FILES) \
            if is_event(request) else forms.ActivityAddForm(request.POST, request.FILES)
        if form_activity_add.is_valid():
            form_activity_add.save()
    return redirect('/events' if is_event(request) else '/')


def update_activity(request, activity_id):
    if request.method == 'POST':
        activity = models.Activity.objects.get(id=activity_id)
        form_activity_update = forms.EventUpdateForm(request.POST, request.FILES, instance=activity) \
            if is_event(request) else forms.ActivityUpdateForm(request.POST, request.FILES, instance=activity)
        if form_activity_update.is_valid():
            form_activity_update.save()
    return redirect('/events' if is_event(request) else '/')


def delete_activity(request, activity_id):
    if request.method == 'POST':
        get_object_or_404(models.Activity, pk=activity_id).delete()
    return redirect('/events' if is_event(request) else '/')


def get_grouped_activities(request):
    activities = {}
    for activity in models.Activity.objects.all().order_by('-id'):
        activity.__dict__['form_activity_update'] = forms.EventUpdateForm(instance=activity) \
            if is_event(request) else forms.ActivityUpdateForm(instance=activity)
        activities.setdefault(activity.type, []).append(activity.__dict__)
    return activities


def is_event(request):
    return '/event' in request.path
