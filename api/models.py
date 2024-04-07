from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    registration_start_date = models.DateTimeField()
    registration_end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    available_seat = models.IntegerField()

    speakers = models.ManyToManyField(
        'Speaker', related_name='events_speaking', blank=True)

    sponsors = models.ManyToManyField(
        'Sponsor', related_name='events_sponsor', blank=True)

    attendees = models.ManyToManyField(
        'Attendee', related_name='events_attending', blank=True)

    schedules = models.ManyToManyField(
        'Schedule', related_name='events_scheduled', blank=True)

    def __str__(self):
        return self.title

    @property
    def status(self):
        if self.start_date < timezone.now():
            return 'passed'
        else:
            return 'upcoming'


class Attendee(models.Model):
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    
    

    def __str__(self):
        return self.fullname


class Speaker(models.Model):
    fullname = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    
    
    def __str__(self):
        return self.fullname


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    

    def __str__(self):
        return self.name


class Schedule(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    activity = models.TextField()

    
    def __str__(self):
        return self.activity
