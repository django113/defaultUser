from django.contrib import admin

# Register your models here.
#
from JobSeekerapp.models import JobSeeker

# admin.site.site_header = 'SVR Admin Site'

GRAPPELLI_ADMIN_TITLE = "SVR Admin Site"
admin.site.site_title = "SVR Admin Site"
admin.site.site_header = "SVR Admin Site"
admin.site.index_title = "SVR Admin Site"

