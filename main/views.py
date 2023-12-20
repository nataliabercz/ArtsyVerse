from django.contrib.auth import models as auth_models
from django.shortcuts import render
from main import models, forms

NAVBAR = {'About': '/about', 'Coaches': '/coaches', 'Events': '/events', 'Gallery': '/gallery', 'Offer': '/offer',
          'Contact': '/contact'}
STUDENT_NAVBAR = {'Assignments': '/user/assignments', 'Chat': '/user/chat', 'Calendar': '/user/calendar',
                  'Payments': '/user/payments', 'Feedback': '/user/feedback', 'Settings': '/user/settings'}
COACH_NAVBAR = {'Chat': '/user/chat', 'Calendar': '/user/calendar', 'Report Absence': '/user/absence',
                'Feedback': '/user/feedback', 'Settings': '/user/settings'}


def get_activities(request):
    return render(request, 'main/main_page/get_activities.html',
                  {'navbar': NAVBAR, 'activities': models.Activity.objects.all()})


def add_activity(request):
    if request.method == 'POST':
        form_add = forms.ActivityForm(request.POST)
        if form_add.is_valid():
            activity = models.Activity(name=request.POST.get('name'))
            activity.save()
    else:
        form_add = forms.ActivityForm()
    # redirect to /activities
    return render(request, 'main/main_page/get_activities.html',
                  {'navbar': NAVBAR, 'activities': models.Activity.objects.all(), 'form_add': form_add})


def update_activity(request):
    form_update = forms.ActivityForm(request.POST or None)
    if form_update.is_valid():
        pass
    # REDIRECT
    return render(request, 'main/main_page/get_activities.html',
                  {'navbar': NAVBAR, 'activities': models.Activity.objects.all(), 'form_add': form_update})


def get_coaches(request):
    return render(request, 'main/main_page/get_coaches.html',
                  {'navbar': NAVBAR, 'coaches': models.CoachProfile.objects.all})


def get_contact(request):
    contacts = {}
    additional_contacts = []
    for coach_profile in models.CoachProfile.objects.all():
        if coach_profile.user.last_name == 'Williams':
            contacts['main_contact'] = coach_profile
        elif coach_profile.user.last_name in ['Gobble']:
            additional_contacts.append(coach_profile)
    contacts['additional_contacts'] = additional_contacts
    return render(request, 'main/main_page/get_contact.html',
                  {'navbar': NAVBAR,
                   'contacts': contacts})


def get_events(request):
    return render(request, 'main/main_page/get_events.html',
                  {'navbar': NAVBAR, 'activities': models.Activity.objects.all()})


def get_gallery(request):
    return render(request, 'main/main_page/get_gallery.html',
                  {'navbar': NAVBAR, 'images': models.Image.objects.all()})


def update_gallery(request):
    if request.method == 'POST':
        form = forms.ImageUpload(request.POST)
        if form.is_valid():
            image = models.Image(image=request.FILES.get('photo'))
            image.save()
    else:
        form = forms.ImageUpload()
    return render(request, 'main/main_page/get_gallery.html',
                  {'navbar': NAVBAR, 'images': models.Image.objects.all(), 'form': form})


def get_info(request):
    return render(request, 'main/main_page/get_info.html', context={'navbar': NAVBAR})


def get_next_classes(request):
    return render(request, 'main/user_page/get_next_classes.html',
                  {'navbar': get_navbar(request.user)})


def get_offer(request):
    grouped_offer = {}
    for item in models.ClassCategory.objects.all():
        for offer in models.Offer.objects.all():
            if item.name.lower() == offer.name.lower():
                grouped_offer[item.name.upper()] = grouped_offer.get(item.name.upper(), {})
                if offer.type == 'individual':
                    grouped_offer[item.name.upper()]['individual'] = grouped_offer[item.name.upper()].get('individual', []) + [offer]
                else:
                    grouped_offer[item.name.upper()]['group'] = grouped_offer[item.name.upper()].get('group', []) + [offer]
    return render(request, 'main/main_page/get_offer.html',
                  {'navbar': NAVBAR, 'grouped_offer': grouped_offer})


def chat(request):
    return render(request, 'main/user_page/chat.html', context={'navbar': get_navbar(request.user)})


def get_calendar(request):
    # option to reschedule (only classes) for coaches
    classes = models.Class.objects.all()
    activities = models.Activity.objects.all()
    calendar_fields = []
    for activity in activities:
        if activity.type == 'Event':
            calendar_fields.append(activity)
    calendar_fields.append(classes)
    return render(request, 'main/user_page/get_calendar.html',
                  {'navbar': get_navbar(request.user), 'events': calendar_fields})


from django.http import JsonResponse


def get_calendar_events(request):
    all_events = models.Events.objects.all()
    out = []
    for event in all_events:
        out.append({
            'title': event.name,
            'id': event.id,
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),
        })

    return JsonResponse(out, safe=False)


def send_feedback(request):
    questions_student = {'How do you like your previous class?': [1, 2, 3], '2': [1, 2], '3': [1, 2, 3], '4': [1, 2]}
    return render(request, 'main/user_page/feedback.html',
                  context={'navbar': get_navbar(request.user),
                           'feedback_questions': questions_student})


def get_settings(request):
    form_change_password = forms.PasswordChangeForm()
    return render(request, 'main/user_page/get_settings.html',
                  {'navbar': get_navbar(request.user), 'form_change_password': form_change_password})


def change_password(request):
    if request.method == 'POST':
        form_change_password = forms.PasswordChangeForm(request.POST)
        if form_change_password.is_valid():
            password = auth_models.UserManager()  # find this
            password.save()
    else:
        form_change_password = forms.PasswordChangeForm()
    return render(request, 'main/user_page/get_settings.html',
                  {'navbar': NAVBAR, 'form_change_password': form_change_password})


def get_assignments(request):
    return render(request, 'main/user_page/assignments.html', context={'navbar': get_navbar(request.user)})


def request_assignments(request):
    pass


def get_payments(request):
    courses = {'Voice Lessons': {'Monthly Price': '$200', 'Left To Pay': '$100'},
               'Dance Lessons': {'Monthly  Price': '$150', 'Left To Pay': '$0'}}
    return render(request, 'main/user_page/payments.html',
                  context={'navbar': get_navbar(request.user),
                           'left_to_pay': '-$100',
                           'courses': courses})


def absence(request):
    questions = {'What is the reason of absence?': ['Sick Leave', 'Other Absence']}
    return render(request, 'main/user_page/absence.html',
                  context={'navbar': get_navbar(request.user),
                           'absence_questions': questions})


def is_student(request_user):
    return 'student.com' in str(request_user)


def get_navbar(request_user):
    if is_student(request_user):
        return STUDENT_NAVBAR
    else:
        return COACH_NAVBAR
