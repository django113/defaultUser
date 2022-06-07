import random

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db import transaction, IntegrityError
from django.forms import modelformset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from JobSeekerapp.forms import JobSeekerForm, WorkForm
from JobSeekerapp.models import Works, JobSeeker, UserOTP

"""
JobSeeker register with otp and login to userdashboard
"""


def JobSeekerregister(request):
    context = {}
    EMployees_count = User.objects.all().count()
    JobSeekers_count = JobSeeker.objects.all().count()

    MarksFormset = modelformset_factory(Works, form=WorkForm)
    form = JobSeekerForm(request.POST or None)
    formset = MarksFormset(request.POST or None, queryset=Works.objects.none(), prefix='works')
    if request.method == "POST":
        get_otp = request.POST.get('otp')  # 213243 #None
        print('1.get otp')

        if get_otp:
            print('2.otp undhi')
            get_usr = request.POST.get('usr')
            print('3.otp theesukundhi')
            usr = JobSeeker.objects.get(username=get_usr)
            print('4.check jobseeker user is ok or not ')
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                print('5.otp user == get otp equal or not')
                messages.success(request, f'Account is Created For {usr.username}')
                print('6.ok otp and user done message send and move login page')
                # note
                # return render(request,'JobSeekerapp/SuccessRegister.html')
                # return  HttpResponse("your successfully Login to Home JobSeeker1")
                return redirect('user-login')

            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                print('7.wrong otp enter')
                return render(request, 'JobSeekerapp/Jobseeker_Registration.html', {'otp': True, 'usr': usr})

        form = JobSeekerForm(request.POST or None)
        formset = MarksFormset(request.POST or None, queryset=Works.objects.none(), prefix='works')

        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    print('8.trasaction atomic')
                    student = form.save(commit=False)
                    print('9.student commit ')
                    student.save()
                    print('10.student save', student)

                    for mark in formset:
                        print('11.formset now work')
                        data = mark.save(commit=False)
                        print('12.work save')
                        data.student = student
                        print('13.student and work move')
                        data.save()
                        print('14.both save')
                        username = form.cleaned_data.get('username')
                        print('15.user name clean', username)
                        email = form.cleaned_data.get('email')
                        print('15.user email clean', email)
                        name = form.cleaned_data.get('name')
                        print('16.name taken', name)
                        usr = JobSeeker.objects.get(username=username)
                        print('17.user object email taking', usr)
                        usr.email = email
                        print('18.user')
                        # usr.username = name[0]
                        # print('19.first name')
                        # if len(name) > 1:
                        #     usr.last_name = name[1]
                        usr.is_active = False
                        usr.save()
                        print('20.usr save ')
                        usr_otp = random.randint(100000, 999999)
                        print('21.otp genrate')
                        UserOTP.objects.create(user=usr, otp=usr_otp)
                        print('22.otp object create')

                        mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

                        send_mail(
                            "Welcome to svr ananthadithya foundation - Verify Your Email",
                            mess,
                            settings.EMAIL_HOST_USER,
                            [usr.email],
                            fail_silently=False
                        )
                        print('23.email send to otp')
                        return render(request, 'JobSeekerapp/Jobseeker_Registration.html', {'otp': True, 'usr': usr})

            except IntegrityError:
                print("Error Encountered")

            # return redirect('account:list')

    context['formset'] = formset
    context['form'] = form
    context['emp'] = (EMployees_count - JobSeekers_count)
    context['job'] = JobSeekers_count
    return render(request, 'JobSeekerapp/Jobseeker_Registration.html', context)


def resend_otp(request):
    if request.method == "GET":
        print('24.resend otp noow')

        # get_usr = request.POST.get('usr')  # 213243 #None
        # print("get user",get_usr)
        get_usr = request.GET['usr']
        print('25.get usr', get_usr)
        if JobSeeker.objects.filter(username=get_usr).exists() and not JobSeeker.objects.get(
                username=get_usr).is_active:
            print('26.get user and jobseeker exist')

            """note"""

            usr = JobSeeker.objects.get(username=get_usr)
            # usr = JobSeeker.objects.get(username=get_usr)
            print('27.checking user jobseeker')
            usr_otp = random.randint(100000, 999999)
            print('28.random gen otp')
            UserOTP.objects.create(user=usr, otp=usr_otp)
            print('29.otp create')
            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to svr ananthadithya foundation - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )
            print('30.otp send')
            return HttpResponse("Resend")

    return HttpResponse("Can't Send ")


def login_view(request):
    print('31.login view')
    if request.user.is_authenticated:
        print('31.is authenticated home to go')
        return redirect('/')
        # return  HttpResponse("your successfully Login to Home JobSeeker2")
    if request.method == 'POST':
        print('32.login post')
        # get_user = request.POST.get('usr')  # 213243 #None
        # print("get user",get_user)
        get_otp = request.POST.get('otp')  # 213243 #None
        print('33.otp get in login')

        if get_otp:
            print('34.otp undhi')
            get_usr = request.POST.get('usr')
            print('35.otp user')
            usr = JobSeeker.objects.get(username=get_usr)
            print('36.jobseeker object create')
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                print('37.user otp save')
                login(request, usr)
                print('38.now otp login  then home,  and success page')
                # note
                return redirect('/')

                # return render(request,'JobSeekerapp/SuccessRegister.html')
                #
                # return  HttpResponse("your successfully Login to Home JobSeeker")
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                print('39.worng otp')
                return render(request, 'JobSeekerapp/login.html', {'otp': True, 'usr': usr})

        # err0r
        usrname = request.POST.get('username')
        passwd = request.POST.get('password')
        print('40.username,password get', usrname, passwd)

        user = authenticate(request, username=usrname, password=passwd)  # None
        if user is not None:
            login(request, user)
            print('41.login now home')
            return redirect('/')

            # return redirect('home')
            # return  HttpResponse("your successfully Login to Home JobSeeker")
        elif not JobSeeker.objects.filter(username=usrname).exists():
            print('42.not exst user send message and then login')
            messages.warning(request,
                             f'Please enter a correct username and password. '
                             f'Note that both fields may be '
                             f'case-sensitive.')
            return redirect('user-login')
        elif not JobSeeker.objects.get(username=usrname).is_active:
            print('43.is active then ')
            usr = JobSeeker.objects.get(username=usrname)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=usr, otp=usr_otp)
            print('44.otp create send msag')
            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to svr ananthadithya foundation - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )
            return render(request, 'JobSeekerapp/login.html', {'otp': True, 'usr': usr})
        else:
            messages.warning(request,
                             f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            print('45.login to go')
            return redirect('user-login')

    form = AuthenticationForm()
    return render(request, 'JobSeekerapp/login.html', {'form': form})


def islogin(request):
    print('is login')
    return JsonResponse({'is_login': request.user.is_authenticated})


# -------------------------------
def JobSeeker_edit(request, pk):
    item = JobSeeker.objects.get(id=pk)
    if request.method == 'POST':
        form = JobSeekerForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = JobSeekerForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)


def JobSeeker_delete(request, pk):
    item = JobSeeker.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)


def JobSeeker_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/products_detail.html', context)
