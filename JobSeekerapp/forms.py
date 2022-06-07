from django import forms
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput

from .models import Works \
    , JobSeeker

from django.contrib.auth import get_user_model

User = get_user_model()


class JobSeekerForm(UserCreationForm):
    # name = forms.CharField(label="Full Name")
    # username = forms.EmailField(label="Email")

    class Meta:
        model = JobSeeker
        # fields = ('name', 'username', 'password1', 'password2')
        fields = [
            'username',
            'email',
            'gender',
            'age',
            'Mother',
            'Father',
            'mobile',
            'location',
            'birth_date',
            'permanent_Address',
            'current_Address',
            'InterestedSector',
            's_name',
            's_study',
            's_grade',
            's_PassOut',
            'i_name',
            'i_study',
            'i_streem',
            'i_grade',
            'i_PassOut',
            'g_name',
            'g_study',
            'g_streem',
            'g_grade',
            'g_PassOut',
            'p_name',
            'p_study',
            'p_streem',
            'p_grade',
            'p_PassOut',
            'exp',
            'company',
            'designation',
            # 'is_approved',
        ]

        labels = {
            'Name': 'Full Name',
            'name': 'Name',
            'username': 'username',
            'gender': 'Gender',
            'age': 'Age',
            'Mother': 'Mother',
            'Father': 'Father',
            'mobile': 'Mobile',
            'location': 'Location',
            'birth_date': 'Date Of Birth',
            'permanent_Address': 'Perminent Address',
            'current_Address': 'Current Address',
            'InterestedSector': 'Interested sector',
            's_name': 'SchoolName',
            's_study': 'School Study',
            's_grade': 'School Grade',
            's_PassOut': 'School Passed Out',
            'i_name': 'Inter College Name',
            'i_study': 'Inter College Study',
            'i_streem': 'Inter College Stream',
            'i_grade': 'Inter College Grade',
            'i_PassOut': 'Inter College Passed Out',
            'g_name': 'Degree College Name ',
            'g_study': 'Degree College Study',
            'g_streem': 'Degree College Stream',
            'g_grade': 'Degree College Grade',
            'g_PassOut': 'Degree College Passed Out',
            'p_name': 'Post Graduate College Name',
            'p_study': 'Post Graduate College Study',
            'p_streem': 'Post Graduate College Stream',
            'p_grade': 'Post Graduate College Grade',
            'p_PassOut': 'Post Graduate College Passed Out',
            'exp': 'Experience',
            'company': 'Company',
            'designation': 'Destination',
            # 'is_approved': 'Approve',
        }
        widgets = {
            'birth_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            's_PassOut': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'i_PassOut': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'g_PassOut': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'p_PassOut': DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


#

class WorkForm(forms.ModelForm):
    # From = DateInput()
    # To = DateInput()

    class Meta:
        model = Works

        fields = [
            'From',
            'To',
        ]

        widgets = {
            'From': forms.TextInput(attrs={'class': 'formset-field'}),
            'To': forms.TextInput(attrs={'class': 'formset-field'}),

        }

# ====================================jobseeker forms======================================================
