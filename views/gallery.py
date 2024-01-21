from django.shortcuts import render, redirect, get_object_or_404
from main import models, forms

HTML_TEMPLATE = 'main/main_page/gallery.html'


def get_gallery(request):
    return render(request, HTML_TEMPLATE, {'images': models.GalleryImage.objects.all().order_by('-id'),
                                           'form_gallery_image_upload': forms.GalleryImageForm()})


def add_image(request):
    if request.method == 'POST':
        form_gallery_image_upload = forms.GalleryImageForm(request.POST, request.FILES)
        if form_gallery_image_upload.is_valid():
            form_gallery_image_upload.save()
    return redirect('/gallery')


def delete_image(request, image_id):
    if request.method == 'POST':
        get_object_or_404(models.GalleryImage, pk=image_id).delete()
    return redirect('/gallery')
