from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from main import models, forms

HTML_TEMPLATE = 'main/main_page/about.html'


def get_about(request):
    try:
        form_about_update = forms.AboutUpdateForm(instance=models.Info.objects.get(id=models.Info.objects.all()[0].id))
    except IndexError:
        form_about_update = forms.InfoInitialForm()
    return render(request, HTML_TEMPLATE, {'info': models.Info.objects.all(),
                                           'images': models.InfoImage.objects.all(),
                                           'form_info_image_upload': forms.InfoImageUploadForm(),
                                           'form_about_update': form_about_update})


@login_required
def update_about(request):
    if request.method == 'POST':
        try:
            form_about_update = forms.AboutUpdateForm(request.POST, request.FILES,
                                                      instance=models.Info.objects.get(
                                                          id=models.Info.objects.all()[0].id))
        except IndexError:
            form_about_update = forms.InfoInitialForm(request.POST, request.FILES)
        print(form_about_update)
        if form_about_update.is_valid():
            form_about_update.save()
    return redirect('/about')


@login_required
def upload_info_image(request):
    if request.method == 'POST':
        form_info_image_upload = forms.InfoImageUploadForm(request.POST, request.FILES)
        if form_info_image_upload.is_valid():
            form_info_image_upload.save()
    return redirect('/about')


def delete_info_image(request, image_id):
    if request.method == 'POST':
        get_object_or_404(models.InfoImage, pk=image_id).delete()
    return redirect('/about')
