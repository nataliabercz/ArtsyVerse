from django import forms


class ActivityForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50)
    # type = forms.ChoiceField(choices=('Info', 'info'), ('Event', 'event'))
    # description = forms.Textarea()


class ImageUpload(forms.Form):
    image = forms.ImageField()


class MyPasswordChangeForm(forms.Form):
    first_name = forms.CharField(label='First name',
                                 max_length=30,
                                 widget=forms.TextInput(attrs={'class' : 'form-control'}),
                                 required=False)
    last_name = forms.CharField(label='Last name',
                                max_length=30,
                                widget=forms.TextInput(attrs={'class' : 'form-control'}),
                                required=False)
    background = forms.CharField(label='Background',
                                 max_length=500,
                                 widget=forms.Textarea(attrs={'class' : 'form-control'}),
                                 required=True)
