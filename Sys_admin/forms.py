from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.decorators import login_required
from Vehicle_assignment.models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class EmployeeForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type' : 'date'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Employee
        fields = ('dob', 'phone', 'image')

class DriverForm(forms.ModelForm):
    vehicle = forms.ModelChoiceField(queryset=Vehicle.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type' : 'date'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Driver
        fields = ('vehicle' , 'dob', 'phone', 'image')

class OfficerForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control','type' : 'date' }))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Officer
        fields = ('dob', 'phone', 'image')    

class VehicleForm(forms.ModelForm):
    model = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    plate_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    color = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Vehicle
        fields = ('model', 'plate_number', 'color', 'image')


class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = CompanyInfo
        fields =('phone1', 'phone2', 'email1', 'email2' , 'adress' , 'po_box' , 'facebook' , 'twitter' , 'instagram' , 'linkedin')
        widgets = {
            'phone1': forms.TextInput(attrs={'class': 'form-control'}),
            'phone2': forms.TextInput(attrs={'class': 'form-control'}),
            'email1': forms.EmailInput(attrs={'class': 'form-control'}),
            'email2': forms.EmailInput(attrs={'class': 'form-control'}),
            'adress': forms.TextInput(attrs={'class': 'form-control'}),
            'po_box': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin': forms.URLInput(attrs={'class': 'form-control'}),
        }


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ('discription' , 'image')
        widgets = {
            'discription': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'dicription': forms.Textarea(attrs={'class': 'form-control'}),
        }



class RegistryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['driver'].queryset = Driver.objects.filter(avaialabilty=True)

    class Meta:
        model = Registry
        fields = ['driver']
        widgets = {
             'driver': forms.Select(attrs={'class': 'form-control'}),
        }
