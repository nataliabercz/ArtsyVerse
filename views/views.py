from django.contrib import auth
from django.shortcuts import render, redirect

# Feedback -> Settings


def login_user(request):
    # logout should redirect to the same page (if not in Account tab - then HOME)
    if request.method == 'POST':
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            auth.login(request, user)
            return redirect('/user')
    return redirect(request.META.get('HTTP_REFERER'))


def error_404(request, exception):
    return render(request, 'main/404_505.html', status=404)


def error_500(request):
    return render(request, 'main/404_505.html', status=500)
