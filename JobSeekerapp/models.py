from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)
Exp_CHOICES = (
    ("Fresher", "Fresher"),
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
)
Interested_CHOICES = (
    ("IT", "IT"),
    ("NON-IT", "NON-IT"),
)


# class

# Create your models here.
class JobSeeker(User):
    slug = models.CharField(max_length=200, unique=True)
    gender = models.CharField(max_length=16, choices=GENDER, default="Male")
    age = models.CharField(max_length=3)
    Mother = models.CharField(max_length=200)
    Father = models.CharField(max_length=200)
    mobile = models.BigIntegerField(default=0)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(default=timezone.now)
    permanent_Address = models.TextField(max_length=500, null=True, blank=True)
    current_Address = models.TextField(max_length=500, null=True, blank=True)
    InterestedSector = models.CharField(max_length=50, choices=Interested_CHOICES, null=True, blank=True)

    s_name = models.CharField(max_length=400, help_text='**School Name Enter', verbose_name='SSC SCHOOL NAME')
    s_study = models.CharField(max_length=100, help_text="**Ex:SSc..", verbose_name='SCHOOL STUDY?')
    s_grade = models.PositiveSmallIntegerField(help_text='**GRADE or  CGPA Enter', verbose_name='GRADE/CGPA',
                                               default='')
    s_PassOut = models.CharField(max_length=20, default='', help_text='**Year of Pass Out Enter',
                                 verbose_name='Passed Out', )

    i_name = models.CharField(max_length=400, help_text='College Name Enter', null=True, blank=True,
                              verbose_name='INTER COLLEGE NAME ')
    i_study = models.CharField(max_length=100, help_text="Ex:Inter ", null=True, blank=True,
                               verbose_name='COLLEGE IN STUDY?')
    i_streem = models.CharField(max_length=200, help_text='optional(Ex:Mpc', null=True, blank=True,
                                verbose_name='STREAM')
    i_grade = models.PositiveSmallIntegerField(help_text='GRADE or  CGPA Enter', null=True, blank=True,
                                               verbose_name='GRADE/CGPA',
                                               default='')
    i_PassOut = models.CharField(max_length=20, help_text='Year of Pass Out Enter', default='',
                                 verbose_name='Passed Out', null=True, blank=True)

    g_name = models.CharField(max_length=400, help_text='College Name Enter', null=True, blank=True,
                              verbose_name='GRADUATE COLLEGE NAME')
    g_study = models.CharField(max_length=100, help_text="Ex:Graduate", null=True, blank=True,
                               verbose_name='COLLEGE IN STUDY?')
    g_streem = models.CharField(max_length=200, help_text='optional(Ex:Bsc(m.p.cs)', blank=True, verbose_name='STREAM')
    g_grade = models.PositiveSmallIntegerField(help_text='GRADE or  CGPA Enter', null=True, blank=True,
                                               verbose_name='GRADE/CGPA',
                                               default='')
    g_PassOut = models.CharField(max_length=20, help_text='Year of Pass Out Enter', default='',
                                 verbose_name='Passed Out', null=True, blank=True)

    p_name = models.CharField(max_length=400, help_text='College Name Enter', null=True, blank=True,
                              verbose_name='COLLEGE NAME P.G')
    p_study = models.CharField(max_length=100, help_text="Ex:SSc or Inter Enter", null=True, blank=True,
                               verbose_name='COLLEGE IN STUDY?')
    p_streem = models.CharField(max_length=200, help_text='optional(Ex:Bsc(m.p.cs)', null=True, blank=True,
                                verbose_name="STREAM")
    p_grade = models.PositiveSmallIntegerField(help_text='GRADE or  CGPA Enter', null=True, blank=True,
                                               verbose_name='GRADE/CGPA',
                                               default='')
    p_PassOut = models.CharField(max_length=20, help_text='Year of Pass Out Enter', default='',
                                 verbose_name='Passed Out', null=True, blank=True)

    exp = models.CharField(
        max_length=50,
        choices=Exp_CHOICES,
        default='Fresher', null=True, blank=True
    )
    company = models.CharField(max_length=300, null=True, blank=True)
    designation = models.CharField(max_length=400, null=True, blank=True)

    is_approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        super(JobSeeker, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('users:dashboard-JobSeeker_detail', kwargs={'slug': self.slug})

    def get_absolute_url(self):
        return reverse('users:dashboard-JobSeeker_detail', kwargs={'slug': self.slug})


    def __str__(self):
        return str(self.username)



    class Meta:
        verbose_name = 'JobSeeker'
        verbose_name_plural = 'JobSeekers'
        db_table = "jobseekers"

import datetime
YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]

class Works(models.Model):
    student = models.ForeignKey('JobSeeker', related_name="works", on_delete=models.CASCADE)
    From = models.CharField(max_length=12,help_text='YYYY/MM',default='')
    To = models.CharField(max_length=12,help_text='YYYY/MM',default='')

    def __str__(self):
        return str(self.student)


    class Meta:
        db_table = "workexp"


class UserOTP(models.Model):
    user = models.ForeignKey(JobSeeker, on_delete=models.CASCADE,related_name='userotp')
    time_st = models.DateTimeField(auto_now=True)
    otp = models.SmallIntegerField()

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'OTPtb'
