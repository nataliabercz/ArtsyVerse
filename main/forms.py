from django.contrib.auth import forms as auth_forms
from django import forms
from main import models


class LoginForm(auth_forms.AuthenticationForm):
    # password should be *********
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField()
    password = forms.PasswordInput()


class ActivityAddForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        exclude = ['start_time', 'end_time', 'location']
        fields = '__all__'
        # widgets = {
        #     'type': forms.TextInput(attrs={'readonly': True, 'value': 'info'})
        # }


class ActivityUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'photo', 'description']


class CoachUpdateForm(forms.ModelForm):
    class Meta:
        model = models.CoachProfile
        fields = ['description']


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = '__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        models = models.Feedback
        fields = '__all__'


class PasswordChangeForm(forms.Form):
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
