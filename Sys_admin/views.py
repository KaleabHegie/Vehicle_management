from django.shortcuts import render
from .models import *
import json
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate , login as auth_login 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from Vehicle_assignment.decorators import *
from django.core.mail import send_mail
from django.conf import settings
from Vehicle_management_system.settings import EMAIL_HOST_USER



import plotly.graph_objs as go
from django.shortcuts import render


from email.message import EmailMessage
import ssl
import smtplib 





# Create your views here.
@login_required
@admin_user_required
def admin_index(request):
    graph = [Employee.objects.count(),Officer.objects.count(),Vehicle.objects.count(),Driver.objects.count()]
   
    context ={
        'employee': Employee.objects.all(),
        'officer': Officer.objects.all(),
        'vehicles': Vehicle.objects.all(),
        'employee_count': Employee.objects.count(),
        'officer_count': Officer.objects.count(),
        'vehicle_count': Vehicle.objects.count(),
        'driver_count':  Driver.objects.count(),
        'message': Messages.objects.all(),
        'message_count': Messages.objects.count(),
        'graph':graph
    }
    return render(request, 'Sys_admin/index.html' , context )

@login_required
@admin_user_required
def register_view_emoloyee(request):

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        employee_form = EmployeeForm(request.POST, request.FILES)

        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save(commit=False)
            user.is_employee = True
            user.save()
            employee = employee_form.save(commit=False)
            employee.customuser = user
            employee.save()
            return redirect ('/sys_admin')
    else:
        user_form = CustomUserCreationForm()
        employee_form = EmployeeForm()
    return render(request, 'Sys_admin/form_employee.html', {'user_form': user_form, 'employee_form': employee_form})


@login_required
@admin_user_required
def register_view_officer(request):

    if request.method == 'POST':
      user_form = CustomUserCreationForm(request.POST)
      officer_form = OfficerForm(request.POST, request.FILES)

      if user_form.is_valid() and officer_form.is_valid():
            user = user_form.save(commit=False)
            user.is_officer = True
            user.save()
            officer = officer_form.save(commit=False)
            officer.customuser = user
            officer.save()
            return redirect ('/sys_admin/')
    else:
        user_form = CustomUserCreationForm()
        officer_form = OfficerForm()
    return render(request, 'Sys_admin/form_officer.html', {'user_form': user_form, 'officer_form': officer_form})



@login_required
@admin_user_required
def register_view_driver(request):

    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        driver_form = DriverForm(request.POST, request.FILES)
        if user_form.is_valid() and driver_form.is_valid():
            user = user_form.save(commit=False)
            user.is_driver = True
            user.save()
            driver = driver_form.save(commit=False)
            driver.customuser = user
            driver.save()
            return redirect ('/sys_admin/')
    else:
        user_form = CustomUserCreationForm()
        driver_form = DriverForm()
    return render(request, 'Sys_admin/form_driver.html', {'user_form': user_form, 'driver_form': driver_form})


@login_required
@admin_user_required
def register_view_vehicle(request):
    if request.method == 'POST':
      vehicle_form = VehicleForm(request.POST, request.FILES)
      if vehicle_form.is_valid(): 
            vehicle = vehicle_form.save(commit=False)
            vehicle.save()
            return redirect ('/sys_admin/')
    else:
        vehicle_form = VehicleForm()
    return render(request, 'Sys_admin/form_vehicle.html', {'vehicle_form': vehicle_form})


@login_required
@admin_user_required
def edit_company_info(request, pk):
    info = CompanyInfo.objects.get(id=pk)
    form = CompanyInfoForm(instance=info)
    
    if request.method == 'POST':
        form = CompanyInfoForm(request.POST, instance=info)
        if form.is_valid():
            form.save()
            return redirect('company_info')
    
    context = {
        'form': form,
        'info': info,
    }
    
    return render(request, 'Sys_admin/edit_company_info.html', context)







@login_required
@officer_user_required
def edit_registry(request, pk):
    try: officer = Officer.objects.get(customuser = request.user)
    except: officer = None
    registry = Registry.objects.get(id=pk)
    form = RegistryForm(instance=registry)
    if request.method == 'POST':
        form = RegistryForm(request.POST, instance=registry)
        if form.is_valid():
            registry.officer = officer            
            registry.driver.avaialabilty = False
            registry.driver.save()
            form.save()
            driver_email = registry.driver.customuser.email
            employee_email = registry.employee.customuser.email
            if employee_email:
                send_mail(
                    'Your vehicle is ready',
                    f'Your trip has been approved. Your drivers name is {registry.driver} with car {registry.driver.vehicle.color} {registry.driver.vehicle.model} with {registry.driver.vehicle} plate number',
                    EMAIL_HOST_USER,
                    [employee_email],
                    fail_silently=False,
                )
            if driver_email:
                send_mail(
                    'You have been assigned',
                    f'You have been assigned to take {registry.employee.customuser.first_name} from {registry.pick_up} to {registry.drop_off} with return time {registry.return_time}',
                    EMAIL_HOST_USER,
                    [driver_email],
                    fail_silently=False,
                )
            return redirect('officer')
    else:
        form = RegistryForm(instance=registry)
    return render(request, 'Sys_admin/approve_registry.html', {'form': form})

   



@login_required
@admin_user_required
def edit_slider(request, pk):
    slider = Slider.objects.get(id=pk)
    form = SliderForm(instance=slider)
    
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=slider)
        if form.is_valid():
            form.save()
            return redirect('slider')
    
    context = {
        'form': form,
        'slider': slider,
    }
    
    return render(request, 'Sys_admin/edit_slider.html', context)



@login_required
@admin_user_required
def add_service(request):
    form = ServiceForm()
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    
    context = {
        'form': form,
    }
    
    return render(request, 'Sys_admin/add_service.html', context)


@login_required
@officer_user_required
def officer(request):
    context = {
        'reg':Registry.objects.all(),
    }
    return render(request, 'Sys_admin/officer.html' , context)
    


@login_required
@admin_user_required
def inbox_view(request):
    context = {
        'message':Messages.objects.all(),
    }
    return render(request, 'Sys_admin/inbox.html' , context)
