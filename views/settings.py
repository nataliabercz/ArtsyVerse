from django.contrib.auth.decorators import login_required
from django.contrib.auth import models as auth_models
from django.shortcuts import render
from main import forms


@login_required
def get_settings(request):
    form_change_password = forms.PasswordChangeForm()
    return render(request, 'main/user_page/settings.html', {'form_change_password': form_change_password})


def update_password(request):
    if request.method == 'POST':
        form_change_password = forms.PasswordChangeForm(request.POST)
        if form_change_password.is_valid():
            password = auth_models.UserManager()  # find this
            password.save()
    else:
        form_change_password = forms.PasswordChangeForm()
    return render(request, 'main/user_page/settings.html', {'form_change_password': form_change_password})


def update_font(request):
    pass


def update_chat_notifications(request):
    pass
