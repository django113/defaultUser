from django.contrib import admin

# Register your models here.
from JobSeekerapp.models import JobSeeker


class HrAdmin(admin.AdminSite):
    site_title = 'Hr Admin Site'
    site_header = 'Hr Admin Site'


GRAPPELLI_ADMIN_TITLE = 'Hr Admin Site'
Hr_site = HrAdmin(name='Hr Admin Site')


# @admin.register(JobSeeker)
class HrJobseekerUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'date_joined']
    # readonly_fields = ['is_staff', ]
    prepopulated_fields = {"slug": ("username",)}

    exclude = ('is_staff', 'user_permissions', 'groups', 'last_login', 'is_superuser')


Hr_site.register(JobSeeker, HrJobseekerUser)
