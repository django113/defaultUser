from django.contrib import admin

# Register your models here.
from JobSeekerapp.models import JobSeeker


class MisAdmin(admin.AdminSite):
    site_title = 'MIS Admin Site'
    site_header = 'MIS Admin Site'


from import_export.admin import ImportExportActionModelAdmin, ExportActionMixin


class MisJobseekerUser(ExportActionMixin, admin.ModelAdmin):
    list_display = ['username', 'email', 'is_staff', 'date_joined']
    readonly_fields = ['is_staff', ]
    prepopulated_fields = {"slug": ("username",)}
    list_filter = ('username', 'age')
    search_fields = ['s_study', 'p_study', 'g_study', 'i_study']
    list_per_page = 10

    exclude = ('is_staff', 'user_permissions', 'groups', 'last_login', 'is_superuser')


GRAPPELLI_ADMIN_TITLE = 'MIS Admin Site'

mis_site = MisAdmin(name='MIS Admin Site')
mis_site.register(JobSeeker, MisJobseekerUser)
