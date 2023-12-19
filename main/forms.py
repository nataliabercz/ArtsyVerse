from django import forms


class ActivityForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    # type = forms.ChoiceField(choices=('Info', 'info'), ('Event', 'event'))
    # description = forms.Textarea()


class ImageUpload(forms.Form):
    image = forms.ImageField()
