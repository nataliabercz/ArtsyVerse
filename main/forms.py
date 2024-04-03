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


class PasswordResetForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Personal Email'}), label='')

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)


class InfoImageUploadForm(forms.ModelForm):
    class Meta:
        model = models.InfoImage
        fields = '__all__'
        labels = {'image': ''}


class InfoInitialForm(forms.ModelForm):
    email_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Email Password'}), label='')

    class Meta:
        model = models.Info
        fields = '__all__'
        labels = {'school_name': '', 'street': '', 'city': '', 'state': '', 'zipcode': '', 'email': '', 'slogan': '',
                  'description': ''}
        widgets = {'school_name': forms.TextInput(attrs={'placeholder': 'School Name'}),
                   'street': forms.TextInput(attrs={'placeholder': 'Street'}),
                   'city': forms.TextInput(attrs={'placeholder': 'City'}),
                   'state': forms.TextInput(attrs={'placeholder': 'State'}),
                   'zipcode': forms.TextInput(attrs={'placeholder': 'Zipcode'}),
                   'email': forms.TextInput(attrs={'placeholder': 'Email'}),
                   'contact_people': forms.MultipleHiddenInput(),
                   'slogan': forms.TextInput(attrs={'placeholder': 'Slogan'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'})}


class AboutUpdateForm(forms.ModelForm):
    email_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Email Password'}), label='')

    class Meta:
        model = models.Info
        fields = '__all__'
        labels = {'school_name': '', 'slogan': '', 'email': '', 'description': ''}
        widgets = {'school_name': forms.TextInput(attrs={'placeholder': 'School Name'}),
                   'street': forms.HiddenInput(),
                   'city': forms.HiddenInput(),
                   'state': forms.HiddenInput(),
                   'zipcode': forms.HiddenInput(),
                   'email': forms.TextInput(attrs={'placeholder': 'Email'}),
                   'contact_people': forms.MultipleHiddenInput(),
                   'slogan': forms.TextInput(attrs={'placeholder': 'Slogan'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'})}


class ContactUpdateForm(forms.ModelForm):
    logo = forms.CharField(widget=forms.HiddenInput())
    favicon = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = models.Info
        fields = '__all__'
        labels = {'street': '', 'city': '', 'state': '', 'zipcode': ''}
        widgets = {'school_name': forms.HiddenInput(),
                   'street': forms.TextInput(attrs={'placeholder': 'Street'}),
                   'city': forms.TextInput(attrs={'placeholder': 'City'}),
                   'state': forms.TextInput(attrs={'placeholder': 'State'}),
                   'zipcode': forms.TextInput(attrs={'placeholder': 'Zipcode'}),
                   'email': forms.HiddenInput(),
                   'email_password': forms.HiddenInput(),
                   'slogan': forms.HiddenInput(),
                   'description': forms.HiddenInput(),
                   'contact_people': forms.MultipleHiddenInput()}


class ContactPeopleUpdateForm(forms.ModelForm):
    logo = forms.CharField(widget=forms.HiddenInput())
    favicon = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = models.Info
        fields = '__all__'
        labels = {'contact_people': ''}
        widgets = {'school_name': forms.HiddenInput(),
                   'street': forms.HiddenInput(),
                   'city': forms.HiddenInput(),
                   'state': forms.HiddenInput(),
                   'zipcode': forms.HiddenInput(),
                   'email': forms.HiddenInput(),
                   'email_password': forms.HiddenInput(),
                   'slogan': forms.HiddenInput(),
                   'description': forms.HiddenInput(),
                   'contact_people': forms.CheckboxSelectMultiple()}


class ActivityAddForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'type', 'image', 'date', 'description']
        labels = {x: '' for x in fields}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'type': forms.HiddenInput(attrs={'value': 'Activity'}),
                   'date': forms.HiddenInput(attrs={'value': datetime.date.today()}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'})}


class ActivityUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'image', 'date', 'description']
        labels = {x: '' for x in fields}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'type': forms.HiddenInput(attrs={'value': 'Activity'}),
                   'date': forms.HiddenInput(attrs={'value': datetime.date.today()}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'})}


class EventAddForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'type', 'image', 'date', 'description', 'start_time', 'end_time', 'ticket_price', 'location']
        labels = {x: '' for x in fields}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'type': forms.HiddenInput(attrs={'value': 'Event'}),
                   'date': forms.SelectDateWidget(),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
                   'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
                   'ticket_price': forms.NumberInput(attrs={'placeholder': 'Ticket Price'}),
                   'location': forms.TextInput(attrs={'placeholder': 'Location'})}


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Activity
        fields = ['name', 'type', 'image', 'date', 'description', 'start_time', 'end_time', 'ticket_price', 'location']
        labels = {x: '' for x in fields}
        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Name'}),
                   'type': forms.HiddenInput(attrs={'value': 'Event'}),
                   'date': forms.SelectDateWidget(),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
                   'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
                   'ticket_price': forms.NumberInput(attrs={'placeholder': 'Ticket Price'}),
                   'location': forms.TextInput(attrs={'placeholder': 'Location'})}


class UserAddForm(forms.ModelForm):
    class Meta:
        model = auth_models.User
        fields = '__all__'
        labels = ({'first_name': '', 'last_name': '', 'email': '', 'is_superuser': 'School Owner'})
        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
                   'username': forms.HiddenInput(attrs={'value': 'username'}),
                   'email': forms.HiddenInput(attrs={'value': 'email@email.com'}),
                   'password': forms.HiddenInput(attrs={'value': 'password'}),
                   'last_login': forms.HiddenInput(),
                   'user_permissions': forms.HiddenInput(),
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
        labels = ({'personal_email': '', 'street': '', 'city': '', 'state': '', 'zipcode': '', 'phone_number': ''})
        widgets = {'user': forms.HiddenInput(),
                   'personal_email': forms.EmailInput(attrs={'placeholder': 'Personal Email'}),
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
        labels = ({'personal_email': '', 'street': '', 'city': '', 'state': '', 'zipcode': '', 'phone_number': ''})
        widgets = {'user': forms.HiddenInput(),
                   'personal_email': forms.EmailInput(attrs={'placeholder': 'Personal Email'}),
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
        labels = {'account_number': ''}
        widgets = ({'user': forms.HiddenInput(),
                    'balance': forms.HiddenInput(attrs={'value': 0}),
                    'account_number': forms.TextInput(attrs={'placeholder': 'Account Number'})})


class StudentProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.StudentProfile
        fields = ['account_number']
        labels = {x: '' for x in fields}
        widgets = ({'account_number': forms.TextInput(attrs={'placeholder': 'Account Number'})})


class ClassAddForm(forms.ModelForm):
    class Meta:
        model = models.Class
        fields = '__all__'
        labels = {'age_group': 'Age Group', 'details': '', 'day_name': 'Day and Time',
                  'start_time': '', 'end_time': '', 'location': ''}
        widgets = {'level': forms.RadioSelect(),
                   'age_group': forms.RadioSelect(),
                   'day_name': forms.RadioSelect(),  # only day
                   'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
                   'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
                   'location': forms.TextInput(attrs={'placeholder': 'Location'}),
                   'details': forms.TextInput(attrs={'placeholder': 'Additional Details'}),
                   'users': forms.MultipleHiddenInput(),
                   'assignments': forms.MultipleHiddenInput()}


class ClassUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Class
        fields = '__all__'
        labels = {'age_group': 'Age Group', 'details': '', 'day_name': '',
                  'start_time': '', 'end_time': '', 'location': ''}
        widgets = {'offer': forms.HiddenInput(),
                   'level': forms.HiddenInput(),
                   'age_group': forms.HiddenInput(),
                   'day_name': forms.RadioSelect(),
                   'start_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
                   'end_time': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
                   'location': forms.TextInput(attrs={'placeholder': 'Location'}),
                   'details': forms.TextInput(attrs={'placeholder': 'Additional Details'}),
                   'users': forms.CheckboxSelectMultiple(),
                   'assignments': forms.MultipleHiddenInput()}


class ClassUsersUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Class
        fields = '__all__'
        labels = {'users': ''}
        widgets = {'offer': forms.HiddenInput(),
                   'level': forms.HiddenInput(),
                   'age_group': forms.HiddenInput(),
                   'day_name': forms.RadioSelect(),
                   'start_time': forms.HiddenInput(),
                   'end_time': forms.HiddenInput(),
                   'location': forms.HiddenInput(),
                   'details': forms.HiddenInput(),
                   'users': forms.CheckboxSelectMultiple(),
                   'assignments': forms.MultipleHiddenInput()}


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = models.GalleryImage
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


class AbsenceRequestForm(forms.ModelForm):
    class Meta:
        model = models.Absence
        fields = '__all__'
        labels = {'reason': '', 'description': ''}
        widgets = ({'start': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
                    'end': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
                    'reason': forms.RadioSelect(),
                    'description': forms.Textarea(attrs={'placeholder': 'Description'})})


class EmailUpdateForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'New Email'}), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Provide Password'}), label='')

    def __init__(self, *args, **kwargs):
        super(EmailUpdateForm, self).__init__(*args, **kwargs)


class PasswordUpdateForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Old Password'}), label='')
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'New Password'}), label='')
    repeated_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}), label='')

    def __init__(self, *args, **kwargs):
        super(PasswordUpdateForm, self).__init__(*args, **kwargs)

    # def validate_project_name(value):
    #     if new_password != repeated_password:
    #         raise ValidationError('This already exists not exist.')
    #     return value
