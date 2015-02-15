from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime

now = datetime.datetime.now()

# Create your models here.   
class Advisory(models.Model):
    GRADE_CHOICES = (
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    )
    name = models.CharField(max_length=50)
    grade = models.IntegerField(choices=GRADE_CHOICES)

    class Meta:
        verbose_name = "Advisory"
        verbose_name_plural = "Advisories"

    def __unicode__(self):
        return self.name

class Staff(models.Model):
    user = models.OneToOneField(User)
    advisory = models.ForeignKey(Advisory)

    PREFIX_CHOICES = (
        ('Mr.','Mr.'),
        ('Ms.','Ms.'),
        ('Mrs.','Mrs.'),
        )
    prefix = models.CharField(max_length=4, choices=PREFIX_CHOICES)    
    

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    def __unicode__(self):
        return self.user.get_full_name()

    def teacher_name(self):
        return "%s %s" %(prefix, last_name)

class Scholar(models.Model):
    GRADE_CHOICES = (
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    grade = models.IntegerField(choices=GRADE_CHOICES)
    advisory = models.ForeignKey(Advisory)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def get_full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __unicode__(self):
        return self.get_full_name()
    

class Referral(models.Model):
    
    REASONS_CHOICES = (
    ('Repeated', 'Repeated Infractions'),
    ('Walkout', 'Walked out'),
    ('Ignored', 'Walked Away/Ignored'),
    ('Language', 'Abusive/Profane Language'),
    ('Bullying', 'Threatening/Bullying'),
    ('Harassment', 'Harassment (sexual, racial, etc.)'),
    ('Preventing', 'Preventing continuation of class'),
    ('Response', 'Inappropriate response to a consequence'),
    ('Horseplay', 'Horseplay'),
    ('Fight', 'Fight'),
    )

    CONSEQUENCE_CHOICES = (
    ('ISS','In School Suspension'),
    ('DET','Detention'),
    ('B2C','Back to Class'),
    ('INV','Investigation'),
        )

    scholar = models.ForeignKey(Scholar)
    staff = models.ForeignKey(Staff)
    datetime = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length = 100, choices=REASONS_CHOICES)
    description = models.CharField(max_length=300, blank=True)
    in_dos = models.BooleanField(default=False)
    consequence = models.CharField(max_length=3, choices=CONSEQUENCE_CHOICES, blank=True)

    def from_today(self):
        return datetime.date == now.date

    def get_absolute_url(self):
        return reverse('referral',kwargs={'pk':self.pk})


    class Meta:
        verbose_name = "Referral"
        verbose_name_plural = "Referrals"
        ordering = ['-datetime','scholar']

    def __unicode__(self):
        return "%s-%s-%s" %(self.pk, self.scholar, self.staff)
    