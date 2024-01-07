import time
import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from main import models

SEASON_START = '2023-09-01'
SEASON_END = '2024-06-30'
OWNER = 'rick.williams@coach.artsyverse.com'  # superuser - no superuser: admin


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
    return render(request, 'main/user_page/calendar.html', {'events': calendar_fields, 'users': users})


def get_calendar_events(request):
    activities = models.Activity.objects.all()
    out = []
    for cls in models.Class.objects.all():
        details = cls.details
        if request.user in cls.users.all() or (request.user.is_superuser and cls.offer.type == 'Group'):
            if cls.offer.type == 'Individual':
                removed_curr_user = cls.users.filter(~Q(email=request.user))[0]
                details = f'{removed_curr_user.first_name} {removed_curr_user.last_name}'
            else:
                for user in cls.users.all():
                    if str(user.groups.all()[0]).lower() == 'coaches':  # is_coach
                        if str(user) != str(request.user):
                            details = f'{user.first_name} {user.last_name}'
                        else:
                            details = f'{cls.level} ({cls.age_group})'
            # for group classes coach instead of None
            for date in get_weekdays(cls.day_name):
                out.append({
                    'id': cls.id,
                    'title': f'{cls.offer.category} ({cls.offer.type[0]})\n{details}\n{cls.location}',
                    'start': datetime.datetime.combine(date, cls.start_time),
                    'end': datetime.datetime.combine(date, cls.end_time),
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
