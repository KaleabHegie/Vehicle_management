from django.http import HttpResponse
from django.shortcuts import redirect
from .models import *
from Account.models import CustomUser

def employee_user_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_employee:            
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to access this content.')
    return wrapper_func

def officer_user_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_officer:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to access this content.')
    return wrapper_func


def admin_user_required(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_superuser:            
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not authorized to access this content.')
    return wrapper_func


