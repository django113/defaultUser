# Generated by Django 4.0.5 on 2022-06-04 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobSeekerapp', '0007_alter_works_from_alter_works_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='From',
            field=models.CharField(help_text='YYYY/MM', max_length=12),
        ),
        migrations.AlterField(
            model_name='works',
            name='To',
            field=models.CharField(help_text='YYYY/MM', max_length=12),
        ),
    ]