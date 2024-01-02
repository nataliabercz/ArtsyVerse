from main import forms

NAVBAR = {'About': '/about', 'Coaches': '/coaches', 'Events': '/events', 'Gallery': '/gallery', 'Offer': '/offer',
          'Contact': '/contact'}
STUDENT_NAVBAR = {'Assignments': '/user/assignments', 'Chat': '/user/chat', 'Calendar': '/user/calendar',
                  'Payments': '/user/payments', 'Settings': '/user/settings'}
COACH_NAVBAR = {'Chat': '/user/chat', 'Calendar': '/user/calendar', 'Request Absence': '/user/absences',
                'Settings': '/user/settings'}
COACH_DOMAIN = 'coach.artsyverse.com'


def set_navbar(request):
    # maybe some regex here
    if '/user' in str(request) or '/login' in str(request) and str(request.user) != 'AnonymousUser':
        if COACH_DOMAIN in str(request.user):
            navbar = COACH_NAVBAR
        else:
            navbar = STUDENT_NAVBAR
    else:
        navbar = NAVBAR
    return {'navbar': navbar}


def login_form(request):
    return {'login_form': forms.LoginForm()}


def image_form(request):
    return {'image_form': forms.ImageForm()}
