from django.shortcuts import render
from main import models

HTML_TEMPLATE = 'main/user_page/student/payments.html'


def get_payments(request):
    balance = 'N/A'
    account_number = 'N/A'
    positive = True
    classes = {}
    for profile in models.StudentProfile.objects.all():
        if str(profile.user) == str(request.user):
            account_number = profile.account_number
            if profile.balance < 0:
                positive = False
            balance = abs(profile.balance)
    for cls in models.Class.objects.all():
        for user in cls.users.all():
            if user == request.user:
                classes[cls.offer.category] = classes.get(cls.offer.category, 0) + cls.offer.monthly_class_price
    return render(request, HTML_TEMPLATE, {'balance': balance, 'positive': positive, 'classes': classes,
                                           'account_number': account_number})


def pay_for_classes(request):
    pass
