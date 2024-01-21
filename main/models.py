import calendar
from django.db import models
from django.contrib.auth import models as auth_models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Activity(BaseModel):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=8, choices=(('Activity', 'Activity'), ('Event', 'Event')))
    image = models.ImageField(upload_to='activities')
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=50)
    ticket_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Activities'


class Offer(BaseModel):
    category = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=(('Individual', 'Individual'), ('Group', 'Group')), default=None)
    single_class_price = models.FloatField(blank=True, null=True)
    monthly_class_price = models.FloatField()
    single_class_description = models.TextField(blank=True, null=True)
    monthly_class_description = models.TextField()
    image = models.ImageField(upload_to='classes')

    def __str__(self):
        return f'{self.category} {self.type}'

    class Meta:
        verbose_name_plural = 'Offer'


class Assignment(BaseModel):
    name = models.CharField(max_length=50)
    skill_degree = models.CharField(max_length=16, choices=(('Requested', 'Requested'), ('Started', 'Started'),
                                                            ('In Progress', 'In Progress'),
                                                            ('Ready To Perform', 'Ready to Perform'),
                                                            ('Obsolete', 'Obsolete')), default=None)
    coach_notes = models.TextField(blank=True)
    student_notes = models.TextField(blank=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(BaseModel):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    level = models.CharField(max_length=12, choices=(('Any', 'Any'), ('Beginner', 'Beginner'),
                                                     ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')),
                             default=None)
    age_group = models.CharField(max_length=10, choices=(('Any', 'Any'), ('Youth', 'Youth'), ('Adults', 'Adults')),
                                 default=None)
    details = models.CharField(max_length=20, blank=True)
    day_name = models.CharField(max_length=9, choices=[(calendar.day_name[i], calendar.day_name[i]) for i in range(0, 5)])
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=20)
    users = models.ManyToManyField(auth_models.User, blank=True)
    assignments = models.ManyToManyField(Assignment, blank=True)

    def __str__(self):
        return f'{self.offer.category} - {self.offer.type} - {self.level} - ' \
               f'{self.age_group} - {self.details} - {self.start_time}'

    class Meta:
        verbose_name_plural = 'Classes'


class Message(BaseModel):
    recipient = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    is_read = models.BooleanField()
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'


class UserProfile(BaseModel):
    user = models.OneToOneField(auth_models.User, on_delete=models.CASCADE)
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=12)
    messages = models.ManyToManyField(Message, blank=True)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name_plural = 'User Profiles'


class CoachProfile(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coaches')
    description = models.TextField()

    def __str__(self):
        return f'{self.user.user.username}'

    class Meta:
        verbose_name_plural = 'Coach Profiles'


class InfoImage(BaseModel):
    image = models.ImageField(upload_to='info')


class Info(BaseModel):
    school_name = models.CharField(max_length=30)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    contact_people = models.ManyToManyField(CoachProfile, blank=True)
    slogan = models.CharField(max_length=80, blank=True)
    logo = models.ImageField(upload_to='info')
    favicon = models.ImageField(upload_to='info')
    description = models.TextField()

    def __str__(self):
        return f'{self.school_name} {self.slogan}'

    class Meta:
        verbose_name_plural = 'Info'


class StudentProfile(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    balance = models.FloatField()

    def __str__(self):
        return f'{self.user.user.username}'

    class Meta:
        verbose_name_plural = 'Student Profiles'


class GalleryImage(BaseModel):
    image = models.ImageField(upload_to='gallery')


class Absence(BaseModel):
    start = models.DateTimeField()
    end = models.DateTimeField()
    reason = models.CharField(max_length=10, choices=(('Sick Leave', 'Sick Leave'), ('Other', 'Other')), default=None)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.reason

# class Setting(BaseModel):
#     pass
#
#
