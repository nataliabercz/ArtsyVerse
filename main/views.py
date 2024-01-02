import time
import datetime
from django.contrib.auth import models as auth_models
from django.contrib import auth
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import Q
from main import models, forms


ADDRESS = {'Street': '3443 Lee Avenue', 'City': 'Laurel Springs', 'State': 'New Jersey', 'Zipcode': '08021'}
CLASSES = {'SINGING', 'PIANO', 'GUITAR', 'DRUMS', 'MUSIC PRODUCTION', 'THEATER', 'DANCING'}
SEASON_START = '2023-09-01'
SEASON_END = '2024-06-30'
OWNER = 'rick.williams@coach.artsyverse.com'
# Feedback -> Settings


def login_user(request):
    # logout should redirect to the same page (if not in Account tab - then HOME)
    if request.method == 'POST':
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        # is the if user needed?
        if user:
            auth.login(request, user)
    return redirect('/user')


def get_activities(request):
    form_add_activity = forms.ActivityAddForm()
    form_update_activity = forms.ActivityUpdateForm()
    return render(request, 'main/main_page/get_activities.html',
                  {'activities': models.Activity.objects.all().order_by('-id'), 'activity_type': 'Info',
                   'form_add_activity': form_add_activity, 'form_update_activity': form_update_activity})


def add_activity(request):
    if request.method == 'POST':
        form_add_activity = forms.ActivityAddForm(request.POST, request.FILES)
        if form_add_activity.is_valid():
            form_add_activity.save()
        return redirect('/')
    else:
        form_add_activity = forms.ActivityAddForm()
    return render(request, 'main/main_page/get_activities.html',
                  {'activities': models.Activity.objects.all().order_by('-id'), 'form_add_activity': form_add_activity})


def update_activity(request):
    if request.method == 'POST':
        form_update_activity = forms.ActivityUpdateForm(request.POST, request.FILES)
        if form_update_activity.is_valid():
            form_update_activity.save()
        return redirect('')
    else:
        form_update_activity = forms.ActivityUpdateForm()
    return render(request, 'main/main_page/get_activities.html',
                  {'activities': models.Activity.objects.all().order_by('-id'),
                   'form_update_activity': form_update_activity})


def get_coaches(request):
    classes = {}
    coaches = models.CoachProfile.objects.all()
    for coach in coaches:
        for _class in models.Class.objects.all():
            if str(coach) in [str(user) for user in _class.users.all()]:
                classes[coach.user.user.username] = classes.get(coach.user.user.username, []) + \
                                                    [f'{_class.offer.category} lessons']
        classes[coach.user.user.username] = set(classes[coach.user.user.username])
    for profile in models.CoachProfile.objects.all():
        if profile.user.user.username == str(request.user):
            coach_instance = models.CoachProfile.objects.get(id=profile.id)
    try:
        form_update_coach = forms.CoachUpdateForm(instance=coach_instance)
    except UnboundLocalError:
        form_update_coach = forms.CoachUpdateForm()
    return render(request, 'main/main_page/get_coaches.html',
                  {'coaches': coaches, 'classes': classes, 'form_update_coach': form_update_coach})


def update_coach(request):
    for profile in models.CoachProfile.objects.all():
        if profile.user.user.username == str(request.user):
            coach_instance = models.CoachProfile.objects.get(id=profile.id)
    if request.method == 'POST':
        form_update_coach = forms.CoachUpdateForm(request.POST, instance=coach_instance)
        if form_update_coach.is_valid():
            form_update_coach.save()
        return redirect('/coaches')
    else:
        for profile in models.CoachProfile.objects.all():
            if profile.user.user.username == str(request.user):
                coach_instance = models.CoachProfile.objects.get(id=profile.id)
        try:
            form_update_coach = forms.CoachUpdateForm(instance=coach_instance)
        except UnboundLocalError:
            form_update_coach = forms.CoachUpdateForm()
    classes = {}
    coaches = models.CoachProfile.objects.all()
    for coach in coaches:
        for _class in models.Class.objects.all():
            if str(coach) in [str(user) for user in _class.users.all()]:
                classes[coach.user.user.username] = classes.get(coach.user.user.username, []) + \
                                                    [f'{_class.offer.category} lessons']
        classes[coach.user.user.username] = set(classes[coach.user.user.username])
    return render(request, 'main/main_page/get_coaches.html',
                  {'coaches': coaches, 'classes': classes, 'form_update_coach': form_update_coach})


def get_contact(request):
    contacts = {}
    additional_contacts = []
    for coach_profile in models.CoachProfile.objects.all():
        if coach_profile.user.user.last_name == 'Williams':
            contacts['main_contact'] = coach_profile
        elif coach_profile.user.user.last_name in ['Gobble']:
            additional_contacts.append(coach_profile)
    contacts['additional_contacts'] = additional_contacts
    return render(request, 'main/main_page/get_contact.html',
                  {'address': ADDRESS, 'contacts': contacts})


def get_events(request):
    # option to buy ticket
    return render(request, 'main/main_page/get_activities.html',
                  {'activities': models.Activity.objects.all(), 'activity_type': 'Event'})


def get_gallery(request):
    # three photos in a row - create table somehow
    form = forms.ImageForm()
    return render(request, 'main/main_page/get_gallery.html',
                  {'images': models.Image.objects.all().order_by('-id'), 'form_add_photo': form})


def update_gallery(request):
    # add option to delete images
    if request.method == 'POST':
        form_add_photo = forms.ImageForm(request.POST, request.FILES)
        if form_add_photo.is_valid():
            form_add_photo.save()
        return redirect('/gallery')
    else:
        form_add_photo = forms.ImageForm()
    return render(request, 'main/main_page/get_gallery.html',
                  {'images': models.Image.objects.all().order_by('-id'), 'form_add_photo': form_add_photo})


def get_info(request):
    return render(request, 'main/main_page/get_info.html')


def get_next_classes(request):
    # only classes assigned to logged person
    classes = []
    next_week = []
    current_time = datetime.datetime.now().time()
    week_day = datetime.datetime.today().weekday()
    print(models.Class.objects.all())
    print(models.Class.objects.values())
    for _class in models.Class.objects.all():
        user = f'{_class.level} ({_class.age_group})'
        if request.user in _class.users.all():
            if _class.offer.type == 'Individual':
                removed_curr_user = _class.users.filter(~Q(email=request.user))[0]
                user = f'{removed_curr_user.first_name} {removed_curr_user.last_name}'
            if time.strptime(_class.day_name, "%A").tm_wday >= week_day:
                if _class.start_time >= current_time:
                    classes.append({'name': _class.offer.category,
                                    'type': _class.offer.type,
                                    'photo': _class.offer.photo,
                                    'day_name': _class.day_name,
                                    'day_id': time.strptime(_class.day_name, "%A").tm_wday,
                                    'start_time': _class.start_time,
                                    'end_time': _class.end_time,
                                    'location': _class.location,
                                    'user': user})
                elif _class.end_time >= current_time:
                    classes.append({'name': _class.offer.category,
                                    'type': _class.offer.type,
                                    'photo': _class.offer.photo,
                                    'day_name': _class.day_name,
                                    'day_id': time.strptime(_class.day_name, "%A").tm_wday,
                                    'start_time': 'NOW',
                                    'end_time': _class.end_time,
                                    'location': _class.location,
                                    'user': user})
            else:
                next_week.append({'name': _class.offer.category,
                                  'type': _class.offer.type,
                                  'photo': _class.offer.photo,
                                  'day_name': _class.day_name,
                                  'day_id': time.strptime(_class.day_name, "%A").tm_wday,
                                  'start_time': _class.start_time,
                                  'end_time': _class.end_time,
                                  'location': _class.location,
                                  'user': user})
    classes = sorted(classes, key=lambda k: (k['day_id'], k['start_time']))
    next_week = sorted(next_week, key=lambda k: (k['day_id'], k['start_time']))
    classes = classes + next_week
    return render(request, 'main/user_page/get_next_classes.html', {'classes': classes})


def get_offer(request):
    grouped_offer = {}
    for offer in models.Offer.objects.all():
        grouped_offer[offer.category] = grouped_offer.get(offer.category, {})
        if offer.type == 'Individual':
            grouped_offer[offer.category]['Individual'] = grouped_offer[offer.category].get('Individual', []) + [offer]
        else:
            grouped_offer[offer.category]['Group'] = grouped_offer[offer.category].get('Group', []) + [offer]
    return render(request, 'main/main_page/get_offer.html', {'grouped_offer': dict(sorted(grouped_offer.items()))})


def get_chat(request):
    return render(request, 'main/user_page/chat.html')


def get_calendar(request):
    # default view - week
    # option to reschedule (only classes) for coaches
    classes = models.Class.objects.all()
    calendar_fields = []
    users = []
    for activity in models.Activity.objects.all():
        if activity.type == 'Event':
            calendar_fields.append(activity)
    calendar_fields.append(classes)
    return render(request, 'main/user_page/get_calendar.html', {'events': calendar_fields, 'users': users})


def get_calendar_events(request):
    activities = models.Activity.objects.all()
    out = []
    for _class in models.Class.objects.all():
        details = _class.details
        if request.user in _class.users.all() or (str(request.user) == OWNER and _class.offer.type == 'Group'):
            if _class.offer.type == 'Individual':
                removed_curr_user = _class.users.filter(~Q(email=request.user))[0]
                details = f'{removed_curr_user.first_name} {removed_curr_user.last_name}'
            # for group classes coach instead of None
            for date in get_weekdays(_class.day_name):
                out.append({
                    'id': _class.id,
                    'title': f'{_class.offer.category} {_class.offer.type}\n{details}\n{_class.location}',
                    'start': datetime.datetime.combine(date, _class.start_time),
                    'end': datetime.datetime.combine(date, _class.end_time),
                })
    for activity in activities:
        if activity.type == 'Event':
            out.append({
                'id': activity.id,
                'title': f'{activity.name}\n{activity.location}',
                'start': datetime.datetime.combine(activity.date, activity.start_time),
                'end': datetime.datetime.combine(activity.date, activity.end_time),
            })
    return JsonResponse(out, safe=False)


def get_weekdays(day_name):
    date_start = datetime.datetime.strptime(SEASON_START, "%Y-%m-%d")
    date_end = datetime.datetime.strptime(SEASON_END, "%Y-%m-%d")
    result = []
    while date_start <= date_end:
        if date_start.weekday() == time.strptime(day_name, "%A").tm_wday:
            result.append(date_start)
        date_start += datetime.timedelta(days=1)
    return result


def get_settings(request):
    form_change_password = forms.PasswordChangeForm()
    return render(request, 'main/user_page/get_settings.html', {'form_change_password': form_change_password})


def change_password(request):
    if request.method == 'POST':
        form_change_password = forms.PasswordChangeForm(request.POST)
        if form_change_password.is_valid():
            password = auth_models.UserManager()  # find this
            password.save()
    else:
        form_change_password = forms.PasswordChangeForm()
    return render(request, 'main/user_page/get_settings.html', {'form_change_password': form_change_password})


def get_assignments(request):
    assignments = []
    for student in models.StudentProfile.objects.all():
        if str(student) == str(request.user):
            assignments = student.assignments.all()
    return render(request, 'main/user_page/student/get_assignments.html', {'assignments': assignments})


def request_assignment(request):
    pass


def get_payments(request):
    balance = 'N/A'
    positive = True
    classes = {}
    for profile in models.StudentProfile.objects.all():
        if str(profile.user) == str(request.user):
            if profile.balance < 0:
                positive = False
            balance = abs(profile.balance)
    for _class in models.Class.objects.all():
        print(_class)
        for user in _class.users.all():
            if user == request.user:
                classes[_class.offer.category] = classes.get(_class.offer.category, 0) + \
                                                 _class.offer.monthly_class_price
    return render(request, 'main/user_page/student/get_payments.html',
                  {'balance': balance, 'positive': positive, 'classes': classes})


def get_absences(request):
    # get info that request were successful - the page should display past and future absences
    # absence is requested -> accepted -> classes have to be rescheduled -> request is green
    return render(request, 'main/user_page/coach/request_absence.html')


def request_absence(request):
    questions = {'What is the reason of absence?': ['Sick Leave', 'Other Absence']}
    # get info that request were successful - the page should display past and future absences
    # absence is requested -> accepted -> classes have to be rescheduled -> request is green
    return render(request, 'main/user_page/coach/request_absence.html', {'absence_questions': questions})
