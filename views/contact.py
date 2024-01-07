from django.shortcuts import render, redirect
from main import models, forms

HTML_TEMPLATE = 'main/main_page/contact.html'


def get_contact(request):
    return render(request, HTML_TEMPLATE, {'contact_data': get_contact_data()})


def update_contact(request):
    if request.method == 'POST':
        form_contact_update = forms.ContactUpdateForm(request.POST, instance=models.Info.objects.
                                                      get(id=models.Info.objects.all()[0].id))
        if form_contact_update.is_valid():
            form_contact_update.save()
    return redirect('/contact')


def get_contact_data():
    contact_data = {}
    info = models.Info.objects.all()
    for item in ['street', 'city', 'state', 'zipcode']:
        contact_data.setdefault('address', {})[item.capitalize()] = info[0].__dict__[item]
    for contact in info[0].contact_people.all():
        if contact.user.user.is_superuser:
            contact_data['main_contact'] = contact
        else:
            contact_data.setdefault('additional_contacts', []).append(contact)
    contact_data['form_contact_update'] = forms.ContactUpdateForm(instance=models.Info.objects.get(id=info[0].id))
    return contact_data
