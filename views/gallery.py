from django.shortcuts import render, redirect, get_object_or_404
from main import models, forms

HTML_TEMPLATE = 'main/main_page/gallery.html'


def get_gallery(request):
    return render(request, HTML_TEMPLATE, {'images': models.Image.objects.all().order_by('-id'),
                                           'form_image_add': forms.ImageForm()})


def add_image(request):
    if request.method == 'POST':
        form_image_add = forms.ImageForm(request.POST, request.FILES)
        if form_image_add.is_valid():
            form_image_add.save()
    return redirect('/gallery')


def delete_image(request, image_id):
    if request.method == 'POST':
        get_object_or_404(models.Image, pk=image_id).delete()
    return redirect('/gallery')
