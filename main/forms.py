import datetime
from django.contrib.auth import forms as auth_forms
from django import forms
from main import models


TEXT_AREA_WIDGET = forms.Textarea(attrs={'cols': 35, 'rows': 10})


class LoginForm(auth_forms.AuthenticationForm):
    # password should be *********
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField()
    password = forms.PasswordInput()


class AboutUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Info
        fields = '__all__'
        widgets = {'school_name': forms.HiddenInput(), 'slogan': forms.HiddenInput(), 'description': TEXT_AREA_WIDGET,
                   'street': forms.HiddenInput(), 'city': forms.HiddenInput(), 'state': forms.HiddenInput(),
                   'zipcode': forms.HiddenInput(), 'contact_people': forms.MultipleHiddenInput()}


class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Info
        fields = '__all__'
        labels = {'contact_people': 'Contact People'}
        widgets = {'school_name': forms.HiddenInput(), 'slogan': forms.HiddenInput(),
                   'description': forms.HiddenInput()}


class ActivityAddForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'type', 'image', 'description', 'date']
        widgets = {'type': forms.HiddenInput(attrs={'value': 'Activity'}),
                   'date': forms.HiddenInput(attrs={'value': datetime.date.today()}),
                   'description': TEXT_AREA_WIDGET}


class ActivityUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'image', 'description', 'date']
        labels = {'image': ''}
        widgets = {'type': forms.HiddenInput(attrs={'value': 'Activity'}),
                   'date': forms.HiddenInput(attrs={'value': datetime.date.today()}),
                   'description': TEXT_AREA_WIDGET}


class EventAddForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = '__all__'
        labels = {'start_time': 'Start Time', 'end_time': 'End Time'}
        widgets = {'type': forms.HiddenInput(attrs={'value': 'Event'}), 'date': forms.SelectDateWidget(),
                   'description': TEXT_AREA_WIDGET}


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = '__all__'
        labels = {'image': '', 'start_time': 'Start Time', 'end_time': 'End Time'}
        widgets = {'type': forms.HiddenInput(attrs={'value': 'Event'}), 'date': forms.SelectDateWidget(),
                   'description': TEXT_AREA_WIDGET}


class CoachAddForm(forms.ModelForm):
    class Meta:
        model = models.CoachProfile
        fields = '__all__'
        widgets = ({'description': TEXT_AREA_WIDGET})


class CoachUpdateForm(forms.ModelForm):
    # multiline description update
    class Meta:
        model = models.CoachProfile
        fields = ['image', 'description']
        widgets = ({'description': TEXT_AREA_WIDGET})


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = '__all__'


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields = '__all__'


class AssignmentRequestForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = ['name', 'skill_degree', 'offer']
        widgets = {'skill_degree': forms.HiddenInput(attrs={'value': 'Requested'}), 'offer': forms.HiddenInput()}


class AssignmentUpdateCoachForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = '__all__'
        exclude = ['student_notes']
        labels = {'coach_notes': 'Notes'}
        widgets = {'coach_notes': TEXT_AREA_WIDGET, 'offer': forms.HiddenInput()}


class AssignmentUpdateStudentForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = '__all__'
        exclude = ['coach_notes']
        labels = {'student_notes': 'Notes'}
        widgets = {'name': forms.HiddenInput(), 'skill_degree': forms.HiddenInput(),
                   'student_notes': TEXT_AREA_WIDGET, 'offer': forms.HiddenInput()}


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


class OfferAddForm(forms.ModelForm):
    class Meta:
        model = models.Offer
        fields = '__all__'
        widgets = ({'description': TEXT_AREA_WIDGET})


class OfferUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Offer
        fields = '__all__'
        labels = ({'image': ''})
        widgets = ({'type': forms.HiddenInput(), 'description': TEXT_AREA_WIDGET})
