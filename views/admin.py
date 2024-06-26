import time
import secrets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models as auth_models
from django.shortcuts import render, redirect, get_object_or_404
from main import models, forms, email_sender


@login_required
def get_users(request):
    return render(request, 'main/admin_page/users.html', {'grouped_users': get_grouped_users(),
                                                          'form_user_add': forms.UserAddForm(),
                                                          'form_user_profile_add': forms.UserProfileAddForm()})


@login_required
def add_user(request, group_id):
    if request.method == 'POST':
        info = models.Info.objects.all()[0]
        data = request.POST
        data._mutable = True
        data['groups'] = auth_models.Group.objects.get(id=group_id)
        form_user_add = forms.UserAddForm(data)
        if form_user_add.is_valid():
            user = form_user_add.save(commit=False)
            password = secrets.token_urlsafe(8)
            user.set_password(password)
            # UNIQUE constraint failed: auth_user.username
            if auth_models.Group.objects.get(id=group_id).name == 'Coaches':
                group = 'coach'
            else:
                group = 'student'
            user.username = f'{user.first_name.lower()}.{user.last_name.lower()}@{group}.{info.school_name.lower()}.com'
            user.email = user.username
            user.save()
            form_user_add.save()
            data['user'] = user
            form_user_profile_add = forms.UserProfileAddForm(data)
            if form_user_profile_add.is_valid():
                user_profile = form_user_profile_add.save()
                personal_email = user_profile.personal_email
                data['user'] = user_profile
                if group == 'coach':
                    form_profile_add = forms.CoachProfileAddForm(data, request.FILES)
                else:
                    form_profile_add = forms.StudentProfileAddForm(data, request.FILES)
                if form_profile_add.is_valid():
                    form_profile_add.save()
                    email_sender_cls = email_sender.EmailSender(1, info.email, info.email_password,
                                                                user.first_name, personal_email, password)
                    email_sender_cls.prepare_and_send_email()
                else:
                    get_object_or_404(auth_models.User, pk=user.id).delete()
            else:
                get_object_or_404(auth_models.User, pk=user.id).delete()
    return redirect('/user/admin/users')


def update_user(request, group_id, profile_id):
    email_type = 3
    if request.method == 'POST':
        if auth_models.Group.objects.get(id=group_id).name == 'Coaches':
            profile = models.CoachProfile.objects.get(id=profile_id)
            form_profile_update = forms.CoachProfileUpdateForm(request.POST, instance=profile)
            if form_profile_update.is_valid():
                form_profile_update.save()
        else:
            profile = models.StudentProfile.objects.get(id=profile_id)
        form_user_profile_update = forms.UserProfileUpdateForm(
            request.POST, instance=models.UserProfile.objects.get(id=profile.user.id))
        if form_user_profile_update.is_valid():
            form_user_profile_update.save()
        form_user_update = forms.UserUpdateForm(
            request.POST, instance=auth_models.User.objects.get(id=profile.user.user.id))
        if form_user_update.is_valid():
            user = form_user_update.save(commit=False)
            if auth_models.Group.objects.get(id=group_id).name == 'Coaches':
                group = 'coach'
            else:
                group = 'student'
            user.username = f'{user.first_name.lower()}.{user.last_name.lower()}@{group}.artsyverse.com'
            # TODO
            user.email = user.username
            user.save()
            form_user_update.save()
    return redirect('/user/admin/users')


def delete_user(request, group_id, profile_id):
    if request.method == 'POST':
        if auth_models.Group.objects.get(id=group_id).name == 'Coaches':
            user_id = models.CoachProfile.objects.get(id=profile_id).user.user.id
        else:
            user_id = models.StudentProfile.objects.get(id=profile_id).user.user.id
        get_object_or_404(auth_models.User, pk=user_id).delete()
    return redirect('/user/admin/users')


def get_grouped_users():
    groups = auth_models.Group.objects.all()
    if 'Coaches' not in [grp.name for grp in groups]:
        auth_models.Group.objects.create(name='Coaches')
    if 'Students' not in [grp.name for grp in groups]:
        auth_models.Group.objects.create(name='Students')
    users = {'Coaches': {'group_id': auth_models.Group.objects.get(name='Coaches').id,
                         'form_profile_add': forms.CoachProfileAddForm(),
                         'profiles': []},
             'Students': {'group_id': auth_models.Group.objects.get(name='Students').id,
                          'form_profile_add': forms.StudentProfileAddForm(),
                          'profiles': []}}
    for coach_profile in models.CoachProfile.objects.all():
        users['Coaches']['profiles'].append(
            {'last_name': coach_profile.user.user.last_name,
             'first_name': coach_profile.user.user.first_name,
             'profile': coach_profile,
             'form_user_update': forms.UserUpdateForm(instance=coach_profile.user.user),
             'form_user_profile_update': forms.UserProfileUpdateForm(instance=coach_profile.user),
             'form_profile_update': forms.CoachProfileUpdateForm(instance=coach_profile)})
    for student_profile in models.StudentProfile.objects.all():
        users['Students']['profiles'].append(
            {'last_name': student_profile.user.user.last_name,
             'first_name': student_profile.user.user.first_name,
             'profile': student_profile,
             'form_user_update': forms.UserUpdateForm(instance=student_profile.user.user),
             'form_user_profile_update': forms.UserProfileUpdateForm(instance=student_profile.user)})
    for item in ['Coaches', 'Students']:
        users[item]['profiles'] = sorted(users[item]['profiles'], key=lambda x: (x['last_name'], x['first_name']))
    return users


@login_required
def get_classes(request):
    return render(request, 'main/admin_page/classes.html', {'offer': models.Offer.objects.all(),
                                                            'grouped_classes': get_grouped_classes(),
                                                            'form_class_add': forms.ClassAddForm()})


def add_class(request):
    if request.method == 'POST':
        form_class_add = forms.ClassAddForm(request.POST)
        if form_class_add.is_valid():
            form_class_add.save()
    return redirect('/user/admin/classes')


def update_class(request, class_id):
    if request.method == 'POST':
        form_class_update = forms.ClassUpdateForm(request.POST, instance=models.Class.objects.get(id=class_id))
        if form_class_update.is_valid():
            form_class_update.save()
    return redirect('/user/admin/classes')


def delete_class(request, class_id):
    if request.method == 'POST':
        get_object_or_404(models.Class, pk=class_id).delete()
    return redirect('/user/admin/users')


def get_grouped_classes():
    classes = {}
    for cls in models.Class.objects.all().order_by('start_time', 'location'):
        classes_dict = cls.__dict__
        classes_dict['day_id'] = time.strptime(cls.day_name, "%A").tm_wday
        classes_dict['form_class_update'] = forms.ClassUpdateForm(instance=cls)
        classes_dict['form_class_users_update'] = forms.ClassUsersUpdateForm(instance=cls)
        classes_dict.setdefault('users', {})
        for user in cls.users.all():
            group = str(user.groups.all()[0]).lower()
            classes_dict['users'].setdefault(group, [])
            classes_dict['users'][group].append(user)
        classes.setdefault(cls.offer.category, {})
        classes[cls.offer.category].setdefault(cls.offer.type, []).append(classes_dict)
        classes[cls.offer.category][cls.offer.type] = sorted(classes[cls.offer.category][cls.offer.type],
                                                             key=lambda x: x['day_id'])
        classes[cls.offer.category] = dict(sorted(classes[cls.offer.category].items()))
    return dict(sorted(classes.items()))
