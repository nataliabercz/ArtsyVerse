import datetime
from django.contrib.auth import models as auth_models
from django.contrib.auth import forms as auth_forms
from django import forms
from main import models


class LoginForm(auth_forms.AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)


class AboutUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Info
        fields = '__all__'
        labels = {'description': ''}
        widgets = {'school_name': forms.HiddenInput(),
                   'slogan': forms.HiddenInput(),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'street': forms.HiddenInput(),
                   'city': forms.HiddenInput(),
                   'state': forms.HiddenInput(),
                   'zipcode': forms.HiddenInput(),
                   'contact_people': forms.MultipleHiddenInput()}


class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Info
        fields = '__all__'
        labels = {'street': '', 'city': '', 'state': '', 'zipcode': '', 'contact_people': 'Contact People'}
        widgets = {'school_name': forms.HiddenInput(),
                   'slogan': forms.HiddenInput(),
                   'description': forms.HiddenInput(),
                   'street': forms.TextInput(attrs={'placeholder': 'Street'}),
                   'city': forms.TextInput(attrs={'placeholder': 'City'}),
                   'state': forms.TextInput(attrs={'placeholder': 'State'}),
                   'zipcode': forms.TextInput(attrs={'placeholder': 'Zipcode'})}


class ActivityAddForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'type', 'image', 'description', 'date']
        labels = {x: '' for x in fields}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'type': forms.HiddenInput(attrs={'value': 'Activity'}),
                   'date': forms.HiddenInput(attrs={'value': datetime.date.today()}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'})}


class ActivityUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'image', 'description', 'date']
        labels = {x: '' for x in fields}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'type': forms.HiddenInput(attrs={'value': 'Activity'}),
                   'date': forms.HiddenInput(attrs={'value': datetime.date.today()}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'})}


class EventAddForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'type', 'image', 'description', 'date', 'start_time', 'end_time', 'ticket_price', 'location']
        labels = {x: '' for x in fields}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'type': forms.HiddenInput(attrs={'value': 'Event'}),
                   'date': forms.SelectDateWidget(),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'start_time': forms.TimeInput(attrs={'placeholder': 'Start Time'}),
                   'end_time': forms.TimeInput(attrs={'placeholder': 'End Time'}),
                   'ticket_price': forms.NumberInput(attrs={'placeholder': 'Ticket Price'}),
                   'location': forms.TextInput(attrs={'placeholder': 'Location'})}


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'type', 'image', 'description', 'date', 'start_time', 'end_time', 'ticket_price', 'location']
        labels = {x: '' for x in fields}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'type': forms.HiddenInput(attrs={'value': 'Event'}),
                   'date': forms.SelectDateWidget(),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'start_time': forms.TimeInput(attrs={'placeholder': 'Start Time'}),
                   'end_time': forms.TimeInput(attrs={'placeholder': 'End Time'}),
                   'ticket_price': forms.NumberInput(attrs={'placeholder': 'Ticket Price'}),
                   'location': forms.TextInput(attrs={'placeholder': 'Location'})}


class UserAddForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = '__all__'
        labels = ({'first_name': '', 'last_name': '', 'email': ''})
        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
                   'username': forms.HiddenInput(attrs={'value': 'tmp'}),
                   'email': forms.HiddenInput(attrs={'value': 'tmp@tmp.com'}),
                   'password': forms.HiddenInput(attrs={'value': 'tmp'}),
                   'last_login': forms.HiddenInput(),
                   'user_permissions': forms.HiddenInput(),
                   'is_superuser': forms.HiddenInput(attrs={'value': False}),
                   'is_staff': forms.HiddenInput(attrs={'value': False}),
                   'is_active': forms.HiddenInput(attrs={'value': True}),
                   'date_joined': forms.HiddenInput(),
                   'groups': forms.MultipleHiddenInput()}
        help_texts = {'is_superuser': '', 'groups': ''}


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = '__all__'
        labels = ({'first_name': '', 'last_name': ''})
        widgets = {'first_name': forms.TextInput(),
                   'last_name': forms.TextInput(),
                   'username': forms.HiddenInput(),
                   'email': forms.HiddenInput(),
                   'password': forms.HiddenInput(),
                   'last_login': forms.HiddenInput(),
                   'user_permissions': forms.MultipleHiddenInput(),
                   'is_superuser': forms.HiddenInput(),
                   'is_staff': forms.HiddenInput(),
                   'is_active': forms.HiddenInput(),
                   'date_joined': forms.HiddenInput(),
                   'groups': forms.MultipleHiddenInput()}
        help_texts = {'is_superuser': '', 'groups': ''}


class UserProfileAddForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        labels = ({'street': '', 'city': '', 'state': '', 'zipcode': '', 'phone_number': ''})
        widgets = {'user': forms.HiddenInput(),
                   'street': forms.TextInput(attrs={'placeholder': 'Street'}),
                   'city': forms.TextInput(attrs={'placeholder': 'City'}),
                   'state': forms.TextInput(attrs={'placeholder': 'State'}),
                   'zipcode': forms.TextInput(attrs={'placeholder': 'Zipcode'}),
                   'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
                   'messages': forms.MultipleHiddenInput()}


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = '__all__'
        labels = ({'street': '', 'city': '', 'state': '', 'zipcode': '', 'phone_number': ''})
        widgets = {'user': forms.HiddenInput(),
                   'street': forms.TextInput(attrs={'placeholder': 'Street'}),
                   'city': forms.TextInput(attrs={'placeholder': 'City'}),
                   'state': forms.TextInput(attrs={'placeholder': 'State'}),
                   'zipcode': forms.TextInput(attrs={'placeholder': 'Zipcode'}),
                   'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
                   'messages': forms.MultipleHiddenInput()}


class CoachProfileAddForm(forms.ModelForm):
    class Meta:
        model = models.CoachProfile
        fields = '__all__'
        labels = ({'image': '', 'description': ''})
        widgets = ({'user': forms.HiddenInput(),
                    'description': forms.Textarea(attrs={'placeholder': 'Description'})})


class CoachProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.CoachProfile
        fields = ['image', 'description']
        labels = {x: '' for x in fields}
        widgets = ({'description': forms.Textarea(attrs={'placeholder': 'Description'})})


class StudentProfileAddForm(forms.ModelForm):
    class Meta:
        model = models.StudentProfile
        fields = '__all__'
        widgets = ({'user': forms.HiddenInput(),
                    'balance': forms.HiddenInput(attrs={'value': 0})})


class ClassAddForm(forms.ModelForm):
    class Meta:
        model = models.Class
        fields = '__all__'
        labels = {'offer': '', 'age_group': 'Age Group', 'details': '', 'day_name': '', 'start_time': '',
                  'end_time': '', 'location': ''}
        widgets = {'offer': forms.RadioSelect(),
                   'level': forms.RadioSelect(),
                   'age_group': forms.RadioSelect(),
                   'details': forms.TextInput(attrs={'placeholder': 'Details'}),
                   'day_name': forms.DateInput(attrs={'placeholder': 'Day Name'}),  # only day
                   'start_time': forms.TimeInput(attrs={'placeholder': 'Start Time'}),
                   'end_time': forms.TimeInput(attrs={'placeholder': 'End Time'}),
                   'location': forms.TextInput(attrs={'placeholder': 'Location'}),
                   'assignments': forms.MultipleHiddenInput()}


class ClassUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Class
        fields = '__all__'


class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = '__all__'
        labels = {'image': ''}


class AssignmentRequestForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = ['name', 'skill_degree', 'offer']
        labels = {'name': ''}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Assignment Name'}),
                   'skill_degree': forms.HiddenInput(attrs={'value': 'Requested'}),
                   'offer': forms.HiddenInput()}


class AssignmentUpdateCoachForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = '__all__'
        exclude = ['student_notes']
        labels = {'name': '', 'skill_degree': '', 'coach_notes': ''}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Assignment Name'}),
                   'skill_degree': forms.RadioSelect(),
                   'coach_notes': forms.Textarea(attrs={'placeholder': 'Notes'}),
                   'offer': forms.HiddenInput()}


class AssignmentUpdateStudentForm(forms.ModelForm):
    class Meta:
        model = models.Assignment
        fields = '__all__'
        exclude = ['coach_notes']
        labels = {'student_notes': ''}
        widgets = {'name': forms.HiddenInput(),
                   'skill_degree': forms.HiddenInput(),
                   'student_notes': forms.Textarea(attrs={'placeholder': 'Notes'}),
                   'offer': forms.HiddenInput()}


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
        fields = ['category', 'type', 'single_class_price', 'monthly_class_price', 'single_class_description',
                  'monthly_class_description', 'image']
        labels = {x: '' for x in fields}
        widgets = ({'category': forms.TextInput(attrs={'placeholder': 'Offer Name'}),
                    'type': forms.RadioSelect(),
                    'single_class_price': forms.NumberInput(attrs={'placeholder': 'Single Class Price'}),
                    'monthly_class_price': forms.NumberInput(attrs={'placeholder': 'Monthly Class Price'}),
                    'single_class_description': forms.Textarea(attrs={'placeholder': 'Single Class Description'}),
                    'monthly_class_description': forms.Textarea(attrs={'placeholder': 'Monthly Class Description'})})


class OfferUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Offer
        fields = '__all__'
        labels = {'category': '', 'single_class_price': '', 'monthly_class_price': '', 'single_class_description': '',
                  'monthly_class_description': ''}
        # set category in other way (hidden input)
        widgets = ({'category': forms.TextInput(attrs={'placeholder': 'Offer Name'}),
                    'type': forms.HiddenInput(),
                    'single_class_price': forms.NumberInput(attrs={'placeholder': 'Single Class Price'}),
                    'monthly_class_price': forms.NumberInput(attrs={'placeholder': 'Monthly Class Price'}),
                    'single_class_description': forms.Textarea(attrs={'placeholder': 'Description'}),
                    'monthly_class_description': forms.Textarea(attrs={'placeholder': 'Description'})})


class MessageSendForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = '__all__'
        labels = ({'text': ''})
        widgets = ({'recipient': forms.HiddenInput(),
                    'datetime': forms.HiddenInput(attrs={'value': datetime.datetime.now()}),
                    'is_read': forms.HiddenInput(attrs={'value': False}),
                    'text': forms.TextInput(attrs={'placeholder': 'Type your message', 'rows': 1})})
