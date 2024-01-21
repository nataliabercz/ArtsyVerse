from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from main import models, forms

HTML_TEMPLATE = 'main/user_page/coach/absences.html'


@login_required
def get_absences(request):
    # get info that request were successful - the page should display past and future absences
    # absence is requested -> accepted -> classes have to be rescheduled -> request is green
    # see other coaches absences
    return render(request, HTML_TEMPLATE, {'grouped_absences': models.Absence.objects.all(),
                                           'form_absence_request': forms.AbsenceRequestForm()})


@login_required
def request_absence(request):
    if request.method == 'POST':
        form_absence_request = forms.AbsenceRequestForm(request.POST)
        if form_absence_request.is_valid():
            absence = form_absence_request.save()
            models.CoachProfile.objects.get(user=models.UserProfile.objects.get(
                user=request.user)).absences.add(absence)
    return redirect(request.META['HTTP_REFERER'])
