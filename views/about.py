from django.shortcuts import render, redirect
from main import models, forms

HTML_TEMPLATE = 'main/main_page/about.html'


def get_about(request):
    form_about_update = forms.AboutUpdateForm(instance=models.Info.objects.get(id=models.Info.objects.all()[0].id))
    return render(request, HTML_TEMPLATE, {'info': models.Info.objects.all(), 'form_about_update': form_about_update})


def update_about(request):
    if request.method == 'POST':
        form_about_update = forms.AboutUpdateForm(request.POST,
                                                  instance=models.Info.objects.get(id=models.Info.objects.all()[0].id))
        print(form_about_update)
        if form_about_update.is_valid():
            form_about_update.save()
    return redirect('/about')
