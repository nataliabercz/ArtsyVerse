from django.shortcuts import render


def get_absences(request):
    # get info that request were successful - the page should display past and future absences
    # absence is requested -> accepted -> classes have to be rescheduled -> request is green
    # see other coaches absences
    return render(request, 'main/user_page/coach/absences.html')


def request_absence(request):
    questions = {'What is the reason of absence?': ['Sick Leave', 'Other Absence']}
    # get info that request were successful - the page should display past and future absences
    # absence is requested -> accepted -> classes have to be rescheduled -> request is green
    return render(request, 'main/user_page/coach/absences.html', {'absence_questions': questions})
