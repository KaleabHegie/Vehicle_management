from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.forms import PasswordChangeForm

     



class RegistryForm(forms.ModelForm):
    class Meta:
        model = Registry
        fields = ['pick_up', 'drop_off', 'return_time', 'trip_description']
        widgets = {
            'pick_up': forms.TextInput(attrs={'class': 'form-control'}),
            'drop_off': forms.TextInput(attrs={'class': 'form-control'}),
            'return_time': forms.TimeInput(attrs={'type': 'time'}),
            'trip_description': forms.Textarea(attrs={'rows': 3}),
        }




class CustomUserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))



class MessageForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['first_name', 'last_name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})        




class EmployeeReviewForm(forms.ModelForm):
    class Meta:
        model = EmployeeReview
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
