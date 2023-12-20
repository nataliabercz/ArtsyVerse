from django.db import models
from django.contrib.auth import models as auth_models


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Activity(BaseModel):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=5, choices=(('Info', 'info'), ('Event', 'event')))
    description = models.TextField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Activities'


class ClassCategory(BaseModel):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Class Categories'


class Offer(BaseModel):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    level = models.CharField(max_length=30)
    option = models.CharField(max_length=30, blank=True, null=True)
    single_class_price = models.FloatField(blank=True, null=True)
    monthly_class_price = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name + ' - ' + self.type + ' - ' + self.level

    class Meta:
        verbose_name_plural = 'Offer'


class Class(BaseModel):
    offer = models.ForeignKey(Offer, blank=True, on_delete=models.CASCADE)
    #    day_name = models.CharField(max_length=10)
    #    start_time = models.CharField(max_length=5)

    def __str__(self):
        return self.offer.name + ' - ' + self.offer.type + ' - ' + self.offer.level

    class Meta:
        verbose_name_plural = 'Classes'


class CoachProfile(BaseModel):
    user = models.ForeignKey(auth_models.User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)
    classes = models.ManyToManyField(Class)
    avatar = models.ImageField(upload_to='coaches')
    description = models.TextField()

    def __str__(self):
        return self.user.last_name

    class Meta:
        verbose_name_plural = 'Coach Profiles'

#
# class Assignment(BaseModel):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name


# class Payment(BaseModel):
#     balance = models.FloatField()
#
#     def __str__(self):
#         return self.balance


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
# class StudentProfile(BaseModel):
#     classes = models.ManyToManyField(Class)
#
#     class Meta:
#         verbose_name_plural = 'Student Profiles'

class Image(BaseModel):
    image = models.ImageField(upload_to='gallery')


class Events(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)
