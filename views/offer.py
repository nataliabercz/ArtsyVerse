from django.shortcuts import render, redirect, get_object_or_404
from main import models, forms


def get_offer(request):
    return render(request, 'main/main_page/offer.html', {'grouped_offer': get_grouped_offer(),
                                                         'form_offer_add': forms.OfferAddForm()})


def add_offer(request):
    if request.method == 'POST':
        form_offer_add = forms.OfferAddForm(request.POST, request.FILES)
        if form_offer_add.is_valid():
            form_offer_add.save()
    return redirect('/offer')


def update_offer(request, offer_id):
    if request.method == 'POST':
        form_offer_update = forms.OfferUpdateForm(request.POST, request.FILES,
                                                  instance=models.Offer.objects.get(id=offer_id))
        if form_offer_update.is_valid():
            form_offer_update.save()
    return redirect(f'/offer#{offer_id}')


def delete_offer(request, offer_id):
    if request.method == 'POST':
        get_object_or_404(models.Offer, pk=offer_id).delete()
    return redirect('/offer')


def sign_in(request):
    pass


def get_grouped_offer():
    offer = {}
    for item in models.Offer.objects.all().order_by('category'):
        if item.type == 'Group':
            item.__dict__['classes'] = models.Class.objects.filter(offer_id=item.id)
        item.__dict__['form_offer_update'] = forms.OfferUpdateForm(instance=item)
        offer.setdefault(item.category, []).append(item.__dict__)
    return offer
