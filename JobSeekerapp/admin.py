from django.contrib import admin
from django import forms
# Register your models here.
from JobSeekerapp.models import JobSeeker, Works
from import_export.admin import ImportExportActionModelAdmin


class WorkExperienceTabular(admin.StackedInline):
    model = Works
    fields = ['From', 'To']

    # widgets = {'From': forms.DateInput(),
    #            'To': forms.DateInput()}
    #
    # def __init__(self, *args, **kwargs):
    #     super(WorkExperienceTabular, self).__init__(*args, **kwargs)
    #     self.fields['From'].widget = forms.DateInput(attrs={'type': 'date'})
    #     self.fields['To'].widget = forms.DateInput(attrs={'type': 'date'})


@admin.register(JobSeeker)
class JobseekerUser(ImportExportActionModelAdmin, admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined']
    readonly_fields = ['is_staff', ]
    prepopulated_fields = {"slug": ("username",)}
    list_filter = ('username', 'age')
    search_fields = ['s_study', 'p_study', 'g_study', 'i_study']
    list_per_page = 10
    #
    exclude = ('is_staff', 'user_permissions', 'groups', 'last_login', 'is_superuser')
    inlines = [WorkExperienceTabular, ]
