from main import models, forms

NAVBAR = {'About': '/about', 'Coaches': '/coaches', 'Events': '/events', 'Gallery': '/gallery', 'Offer': '/offer',
          'Contact': '/contact'}
STUDENT_NAVBAR = {'Assignments': '/user/assignments', 'Messages': '/user/messages', 'Calendar': '/user/calendar',
                  'Payments': '/user/payments', 'Settings': '/user/settings'}
COACH_NAVBAR = {'Messages': '/user/messages', 'Calendar': '/user/calendar', 'Absences': '/user/absences',
                'Settings': '/user/settings'}


def set_navbar(request):
    school_data = {}
    try:
        info = models.Info.objects.all()[0]
        school_data['name'] = info.school_name
        if info.slogan:
            school_data['slogan'] = f'| {info.slogan}'
        school_data['logo'] = f'/media/{info.logo}'
        school_data['favicon'] = f'/media/{info.favicon}'
    except IndexError:
        school_data['name'] = 'School Name'
        school_data['slogan'] = ' | Slogan'
        school_data['logo'] = '/media/icons/logo_example.png'
        school_data['favicon'] = f'/media/icons/favicon_example.ico'
    # maybe some regex here
    if '/user' in str(request) or '/login' in str(request) and str(request.user) != 'AnonymousUser':
        if 'coach.artsyverse.com' in str(request.user) or request.user.is_superuser:
            # TODO request.user.group == 'Coaches'
            navbar = COACH_NAVBAR
        else:
            navbar = STUDENT_NAVBAR
    else:
        navbar = NAVBAR
    return {'school_data': school_data, 'navbar': navbar}


def login_form(request):
    return {'login_form': forms.LoginForm()}


def password_reset_form(request):
    return {'password_reset_form': forms.PasswordResetForm()}
