import calendar
from django.db import models
from django.contrib.auth import models as auth_models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Activity(BaseModel):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=5, choices=(('Info', 'info'), ('Event', 'event')))
    photo = models.ImageField(upload_to='gallery', blank=True, null=True)
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
    category = models.CharField(max_length=20, choices=(('Singing', 'singing'), ('Piano', 'piano'),
                                                        ('Guitar', 'guitar'), ('Bass', 'bass'), ('Drums', 'drums'),
                                                        ('Music Production', 'music production'), ('Band', 'band'),
                                                        ('Theater', 'theater'), ('Dancing', 'dancing')))
    type = models.CharField(max_length=10, choices=(('Individual', 'individual'), ('Group', 'group')))
    single_class_price = models.FloatField(blank=True, null=True)
    monthly_class_price = models.FloatField(blank=True, null=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='classes', blank=True, null=True)

    def __str__(self):
        return f'{self.category} {self.type}'

    class Meta:
        verbose_name_plural = 'Offer'


class Class(BaseModel):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    level = models.CharField(max_length=12, choices=(('Any', 'any'), ('Beginner', 'beginner'),
                                                     ('Intermediate', 'intermediate'), ('Advanced', 'advanced')))
    age_group = models.CharField(max_length=10, choices=(('Any', 'any'), ('Youth', 'youth'), ('Adults', 'adults')))
    details = models.CharField(max_length=20, blank=True, null=True)
    day_name = models.CharField(max_length=9, choices=[(calendar.day_name[i], calendar.day_name[i]) for i in range(0, 5)])
    start_time = models.TimeField()
    end_time = models.TimeField()
    users = models.ManyToManyField(auth_models.User, blank=True, null=True)
    location = models.CharField(max_length=20)

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
    photo = models.ImageField(upload_to='coaches')
    description = models.TextField()

    def __str__(self):
        return f'{self.user.user.username}'

    class Meta:
        verbose_name_plural = 'Coach Profiles'


class Assignment(BaseModel):
    name = models.CharField(max_length=50)
    skill_degree = models.CharField(max_length=16, choices=(('Requested', 'requested'), ('Started', 'started'),
                                                            ('In Progress', 'in progress'),
                                                            ('Ready To Perform', 'ready to perform')))
    coach_notes = models.TextField(blank=True, null=True)
    student_notes = models.TextField(blank=True, null=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class StudentProfile(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    assignments = models.ManyToManyField(Assignment)
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


# class Calendar(BaseModel):
#     activity = models.ForeignKey(Activity, blank=True, on_delete=models.CASCADE)
#     classes = models.ForeignKey(Class, blank=True, on_delete=models.CASCADE)
#
#     class Meta:
#         verbose_name_plural = 'Calendar'


# class Chat(BaseModel):
#     class Meta:
#         verbose_name_plural = 'Chat'
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
