"""user_proxy_type URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView, PasswordResetConfirmView, \
    PasswordResetDoneView, PasswordResetView
from django.urls import path, include
from Misapp.admin import mis_site
from Hrapp.admin import Hr_site
from JobSeekerapp.views import *
from baton.autodiscover import admin
from django.urls import path, include


urlpatterns = [

    # path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    #
    path('EmployeeLogin/', admin.site.urls),
    path('baton/', include('baton.urls')),
    # path('misadmin/', mis_site.urls),
    # path('hradmin/', Hr_site.urls),
    path('', include('JobSeekerapp.urls')),

    path('login/', login_view, name='user-login'),

    path('logout/', LogoutView.as_view(next_page='user-login'), name='logout'),
    #
    path("password-reset/",
         PasswordResetView.as_view(template_name='JobSeekerapp/password_reset.html'),
         name="password_reset"),

    path("password-reset/done/",
         PasswordResetDoneView.as_view(template_name='JobSeekerapp/password_reset_done.html'),
         name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/",
         PasswordResetConfirmView.as_view(template_name='JobSeekerapp/password_reset_confirm.html'),
         name="password_reset_confirm"),

    path("password-reset-complete/",
         PasswordResetCompleteView.as_view(template_name='JobSeekerapp/password_reset_complete.html'),
         name="password_reset_complete"),

    path('user/resendOTP/', resend_otp),

    path('islogin', islogin),
]

"""
Mnbvcxz@123
"""
