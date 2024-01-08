import calendar
from django.db import models
from django.contrib.auth import models as auth_models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Activity(BaseModel):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=8, choices=(('Activity', 'activity'), ('Event', 'event')))
    image = models.ImageField(upload_to='gallery')
    description = models.TextField()
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Activities'


class Offer(BaseModel):
    category = models.CharField(max_length=20)
    type = models.CharField(max_length=10, choices=(('Individual', 'individual'), ('Group', 'group')))
    single_class_price = models.FloatField(blank=True, null=True)
    monthly_class_price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='classes')

    def __str__(self):
        return f'{self.category} {self.type}'

    class Meta:
        verbose_name_plural = 'Offer'


class Assignment(BaseModel):
    name = models.CharField(max_length=50)
    skill_degree = models.CharField(max_length=16, choices=(('Requested', 'requested'), ('Started', 'started'),
                                                            ('In Progress', 'in progress'),
                                                            ('Ready To Perform', 'ready to perform'),
                                                            ('Obsolete', 'obsolete')))
    coach_notes = models.TextField(blank=True, null=True)
    student_notes = models.TextField(blank=True, null=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(BaseModel):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    level = models.CharField(max_length=12, choices=(('Any', 'any'), ('Beginner', 'beginner'),
                                                     ('Intermediate', 'intermediate'), ('Advanced', 'advanced')))
    age_group = models.CharField(max_length=10, choices=(('Any', 'any'), ('Youth', 'youth'), ('Adults', 'adults')))
    details = models.CharField(max_length=20, blank=True, null=True)
    day_name = models.CharField(max_length=9, choices=[(calendar.day_name[i], calendar.day_name[i]) for i in range(0, 5)])
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=20)
    users = models.ManyToManyField(auth_models.User, blank=True, null=True)
    assignments = models.ManyToManyField(Assignment, blank=True, null=True)

    def __str__(self):
        return f'{self.offer.category} - {self.offer.type} - {self.level} - ' \
               f'{self.age_group} - {self.details} - {self.start_time}'

    class Meta:
        verbose_name_plural = 'Classes'


class UserProfile(BaseModel):
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    street_name = models.CharField(max_length=30)
    city = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.user.username}'

    class Meta:
        verbose_name_plural = 'User Profiles'


class CoachProfile(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='coaches')
    description = models.TextField()

    def __str__(self):
        return f'{self.user.user.username}'

    class Meta:
        verbose_name_plural = 'Coach Profiles'


class Info(BaseModel):
    school_name = models.CharField(max_length=30)
    slogan = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    contact_people = models.ManyToManyField(CoachProfile)

    def __str__(self):
        return f'{self.school_name} {self.slogan}'

    class Meta:
        verbose_name_plural = 'Info'


class StudentProfile(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    balance = models.FloatField()

    def __str__(self):
        return f'{self.user.user.username}'

    class Meta:
        verbose_name_plural = 'Student Profiles'


class Image(BaseModel):
    image = models.ImageField(upload_to='gallery')


class Payment(BaseModel):
    balance = models.FloatField()

    def __str__(self):
        return self.balance


# class Absence(BaseModel):
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     reason = models.Choices('Sick Leave', 'Other Absence')
#     description = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.reason
#
#
# class Feedback(BaseModel):
#     pass
#
#
# class Setting(BaseModel):
#     pass
#
#


# import datetime
# from django.urls import reverse
#
#
# class Event(BaseModel):
#     title = models.CharField(max_length=200)
#     start_time = models.DateTimeField(default=datetime.date.today)
#
#     def __str__(self):
#         return self.title
#
#     @property
#     def get_html_url(self):
#         url = reverse('event_edit', args=(self.id,))
#         return f'<p>{self.title}</p><a href="{url}">edit</a>'


class Feedback(BaseModel):
    question1 = models.CharField(max_length=255)
    answer1 = models.TextField()


class Message(BaseModel):
    sender = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    is_read = models.BooleanField()
    text = models.TextField()
