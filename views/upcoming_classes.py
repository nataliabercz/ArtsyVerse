from django.contrib.auth.decorators import login_required
import time
import datetime
from django.shortcuts import render
from django.db.models import Q
from main import models

HTML_TEMPLATE = 'main/user_page/upcoming_classes.html'


@login_required()
def get_upcoming_classes(request):
    classes = []
    next_week = []
    current_time = datetime.datetime.now().time()
    week_day = datetime.datetime.today().weekday()
    for cls in models.Class.objects.all():
        user = f'{cls.level} ({cls.age_group})'
        user_id = ''
        if request.user in cls.users.all():
            if cls.offer.type == 'Individual':
                removed_curr_user = cls.users.filter(~Q(email=request.user))[0]
                user = f'{removed_curr_user.first_name} {removed_curr_user.last_name}'
                user_id = removed_curr_user.id
            if time.strptime(cls.day_name, "%A").tm_wday >= week_day:
                if cls.start_time >= current_time:
                    classes.append({'name': cls.offer.category,
                                    'type': cls.offer.type,
                                    'image': cls.offer.image,
                                    'day_name': cls.day_name,
                                    'day_id': time.strptime(cls.day_name, "%A").tm_wday,
                                    'start_time': cls.start_time,
                                    'end_time': cls.end_time,
                                    'location': cls.location,
                                    'user': user,
                                    'user_id': user_id,
                                    'class_id': cls.id})
                elif cls.end_time >= current_time:
                    classes.append({'name': cls.offer.category,
                                    'type': cls.offer.type,
                                    'image': cls.offer.image,
                                    'day_name': cls.day_name,
                                    'day_id': time.strptime(cls.day_name, "%A").tm_wday,
                                    'start_time': 'NOW',
                                    'end_time': cls.end_time,
                                    'location': cls.location,
                                    'user': user,
                                    'user_id': user_id,
                                    'class_id': cls.id})
            else:
                next_week.append({'name': cls.offer.category,
                                  'type': cls.offer.type,
                                  'image': cls.offer.image,
                                  'day_name': cls.day_name,
                                  'day_id': time.strptime(cls.day_name, "%A").tm_wday,
                                  'start_time': cls.start_time,
                                  'end_time': cls.end_time,
                                  'location': cls.location,
                                  'user': user,
                                  'user_id': user_id,
                                  'class_id': cls.id})
    classes = sorted(classes, key=lambda x: (x['day_id'], x['start_time']))
    next_week = sorted(next_week, key=lambda x: (x['day_id'], x['start_time']))
    return render(request, HTML_TEMPLATE, {'classes': classes + next_week})
