import secrets
from django.contrib.auth.decorators import login_required
from django.contrib.auth import models as auth_models
from django.shortcuts import render, redirect
from django import forms as django_forms
from main import models, forms, email_sender


@login_required
def get_settings(request):
    form_update_email = forms.EmailUpdateForm()
    form_update_password = forms.PasswordUpdateForm()
    return render(request, 'main/user_page/settings.html', {'form_update_email': form_update_email,
                                                            'form_update_password': form_update_password})


def update_email(request):
    if request.method == 'POST':
        form_update_email = forms.EmailUpdateForm(request.POST)
        if form_update_email.is_valid():
            data = form_update_email.cleaned_data
            email = data['email']
            password = data['password']
            # userprofile here - personal email
            user = auth_models.User.objects.get(id=request.user.id)
            user.password = password
    return redirect('/user/settings')


def reset_password(request):
    if request.method == 'POST':
        form_reset_password = forms.PasswordResetForm(request.POST)
        if form_reset_password.is_valid():
            info = models.Info.objects.all()[0]
            personal_email = form_reset_password.cleaned_data['email']
            password = secrets.token_urlsafe(8)
            email_sender_cls = email_sender.EmailSender(2, info.email, info.email_password, personal_email, password)
            email_sender_cls.prepare_and_send_email()
    return redirect('/')


def update_password(request):
    if request.method == 'POST':
        form_update_password = forms.PasswordUpdateForm(request.POST)
        if form_update_password.is_valid():
            data = form_update_password.cleaned_data
            old_password = data['old_password']
            new_password = data['new_password']
            repeated_password = data['repeated_password']
            if new_password != repeated_password:
                print('Passwords don\'t match.')
            # userprofile here - personal email
            if old_password != request.user.password:
                print('Wrong Password')
            # user.password = new_password
    return redirect('/user/settings')


def update_font(request):
    pass


def update_chat_notifications(request):
    pass
