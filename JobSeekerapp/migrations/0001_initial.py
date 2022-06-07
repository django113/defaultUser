# Generated by Django 4.0.5 on 2022-06-03 08:25

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=16)),
                ('age', models.CharField(max_length=3)),
                ('Mother', models.CharField(max_length=200)),
                ('Father', models.CharField(max_length=200)),
                ('mobile', models.BigIntegerField(default=0)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(default=django.utils.timezone.now)),
                ('permanent_Address', models.TextField(blank=True, max_length=500, null=True)),
                ('current_Address', models.TextField(blank=True, max_length=500, null=True)),
                ('InterestedSector', models.CharField(blank=True, choices=[('IT', 'IT'), ('NON-IT', 'NON-IT')], max_length=50, null=True)),
                ('s_name', models.CharField(help_text='**School Name Enter', max_length=400, verbose_name='SSC SCHOOL NAME')),
                ('s_study', models.CharField(help_text='**Ex:SSc..', max_length=100, verbose_name='SCHOOL STUDY?')),
                ('s_grade', models.PositiveSmallIntegerField(default='', help_text='**GRADE or  CGPA Enter', verbose_name='GRADE/CGPA')),
                ('s_PassOut', models.CharField(default='', help_text='**Year of Pass Out Enter', max_length=20, verbose_name='Passed Out')),
                ('i_name', models.CharField(blank=True, help_text='College Name Enter', max_length=400, null=True, verbose_name='INTER COLLEGE NAME ')),
                ('i_study', models.CharField(blank=True, help_text='Ex:Inter ', max_length=100, null=True, verbose_name='COLLEGE IN STUDY?')),
                ('i_streem', models.CharField(blank=True, help_text='optional(Ex:Mpc', max_length=200, null=True, verbose_name='STREAM')),
                ('i_grade', models.PositiveSmallIntegerField(blank=True, default='', help_text='GRADE or  CGPA Enter', null=True, verbose_name='GRADE/CGPA')),
                ('i_PassOut', models.CharField(blank=True, default='', help_text='Year of Pass Out Enter', max_length=20, null=True, verbose_name='Passed Out')),
                ('g_name', models.CharField(blank=True, help_text='College Name Enter', max_length=400, null=True, verbose_name='GRADUATE COLLEGE NAME')),
                ('g_study', models.CharField(blank=True, help_text='Ex:Graduate', max_length=100, null=True, verbose_name='COLLEGE IN STUDY?')),
                ('g_streem', models.CharField(blank=True, help_text='optional(Ex:Bsc(m.p.cs)', max_length=200, verbose_name='STREAM')),
                ('g_grade', models.PositiveSmallIntegerField(blank=True, default='', help_text='GRADE or  CGPA Enter', null=True, verbose_name='GRADE/CGPA')),
                ('g_PassOut', models.CharField(blank=True, default='', help_text='Year of Pass Out Enter', max_length=20, null=True, verbose_name='Passed Out')),
                ('p_name', models.CharField(blank=True, help_text='College Name Enter', max_length=400, null=True, verbose_name='COLLEGE NAME P.G')),
                ('p_study', models.CharField(blank=True, help_text='Ex:SSc or Inter Enter', max_length=100, null=True, verbose_name='COLLEGE IN STUDY?')),
                ('p_streem', models.CharField(blank=True, help_text='optional(Ex:Bsc(m.p.cs)', max_length=200, null=True, verbose_name='STREAM')),
                ('p_grade', models.PositiveSmallIntegerField(blank=True, default='', help_text='GRADE or  CGPA Enter', null=True, verbose_name='GRADE/CGPA')),
                ('p_PassOut', models.CharField(blank=True, default='', help_text='Year of Pass Out Enter', max_length=20, null=True, verbose_name='Passed Out')),
                ('exp', models.CharField(blank=True, choices=[('Fresher', 'Fresher'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='Fresher', max_length=50, null=True)),
                ('company', models.CharField(blank=True, max_length=300, null=True)),
                ('designation', models.CharField(blank=True, max_length=400, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name': 'JobSeeker',
                'verbose_name_plural': 'JobSeekers',
                'db_table': 'jobseekers',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.CharField(max_length=32)),
                ('To', models.CharField(max_length=3)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='works', to='JobSeekerapp.jobseeker')),
            ],
            options={
                'db_table': 'workexp',
            },
        ),
        migrations.CreateModel(
            name='UserOTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_st', models.DateTimeField(auto_now=True)),
                ('otp', models.SmallIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userotp', to='JobSeekerapp.jobseeker')),
            ],
            options={
                'db_table': 'OTPtb',
            },
        ),
    ]
