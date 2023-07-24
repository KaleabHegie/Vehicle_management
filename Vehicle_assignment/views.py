from django.shortcuts import render
from .models import *
import json
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login , logout
from django.contrib.auth import authenticate , login as auth_login 
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .decorators import *

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy


    


def index(request):
    

#     car_data ={
#     "cars": [
#         {
#             "model": "Toyota Camry",
#             "plate_number": "ABC-1234",
#             "color": "red",
#             "image": "https://example.com/cars/toyota_camry_red.jpg"
#         },
#         {
#             "model": "Honda Civic",
#             "plate_number": "DEF-5678",
#             "color": "blue",
#             "image": "https://example.com/cars/honda_civic_blue.jpg"
#         },
#         {
#             "model": "Ford Mustang",
#             "plate_number": "GHI-9101",
#             "color": "yellow",
#             "image": "https://example.com/cars/ford_mustang_yellow.jpg"
#         },
#         {
#             "model": "Chevrolet Corvette",
#             "plate_number": "JKL-2345",
#             "color": "black",
#             "image": "https://example.com/cars/chevrolet_corvette_black.jpg"
#         },
#         {
#             "model": "Nissan Altima",
#             "plate_number": "MNO-6789",
#             "color": "silver",
#             "image": "https://example.com/cars/nissan_altima_silver.jpg"
#         },
#         {
#             "model": "BMW 3 Series",
#             "plate_number": "PQR-1234",
#             "color": "white",
#             "image": "https://example.com/cars/bmw_3_series_white.jpg"
#         },
#         {
#             "model": "Audi A4",
#             "plate_number": "STU-5678",
#             "color": "blue",
#             "image": "https://example.com/cars/audi_a4_blue.jpg"
#         },
#         {
#             "model": "Mercedes-Benz C-Class",
#             "plate_number": "VWX-9101",
#             "color": "silver",
#             "image": "https://example.com/cars/mercedes_benz_c_class_silver.jpg"
#         },
#         {
#             "model": "Tesla Model S",
#             "plate_number": "YZA-2345",
#             "color": "red",
#             "image": "https://example.com/cars/tesla_model_s_red.jpg"
#         },
#         {
#             "model": "Porsche 911",
#             "plate_number": "BCD-6789",
#             "color": "black",
#             "image": "https://example.com/cars/porsche_911_black.jpg"
#         },
#         {
#             "model": "Lamborghini Huracan",
#             "plate_number": "EFG-1234",
#             "color": "yellow",
#             "image": "https://example.com/cars/lamborghini_huracan_yellow.jpg"
#         },
#         {
#             "model": "Ferrari 488 GTB",
#             "plate_number": "HIJ-5678",
#             "color": "red",
#             "image": "https://example.com/cars/ferrari_488_gtb_red.jpg"
#         },
#         {
#             "model": "McLaren 720S",
#             "plate_number": "KLM-9101",
#             "color": "orange",
#             "image": "https://example.com/cars/mclaren_720s_orange.jpg"
#         },
#         {
#             "model": "Bugatti Chiron",
#             "plate_number": "NOP-2345",
#             "color": "blue",
#             "image": "https://example.com/cars/bugatti_chiron_blue.jpg"
#         }
#     ]
# }

#     for car_entry in car_data['cars']:
#         vehicle = Vehicle.objects.create(
#             model=car_entry['model'],
#             plate_number=car_entry['plate_number'],
#             color=car_entry['color'],
#             image=car_entry['image']
#         )

#     vehicle.objects.save()
    


    context = {
        
        'data':CompanyInfo.objects.all(),
        'slider':Slider.objects.all(),
        'cars':Vehicle.objects.all(),
        
    }
    return render(request, 'Vehicle_assignment/index-cars.html', context) 


@login_required
@employee_user_required
def add_registry(request):
    try: employee = Employee.objects.get(customuser = request.user)
    except: employee = None
    try: registry = Registry.objects.get(employee = request.user)
    except: registry = None


    if request.method == 'POST' and (registry is None or registry.status is False):
        form = RegistryForm(request.POST)
        if form.is_valid():
            registry = form.save(commit=False)
            registry.employee = employee
            registry.status = True
            registry.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect('index')
    else:
        form = RegistryForm()
        messages.success(request, 'You either are already using a vhicle or requested for one.')
        return redirect('index')
    
    context = {
        'form': form,
       } 
     
    return render(request, 'Vehicle_assignment/reg.html', context)
   

def service(request):
    context = {
        'data':CompanyInfo.objects.all(),
        'service':Service.objects.all(),
        
    }
    return render(request, 'Vehicle_assignment/service.html' , context)

def service_details(request):
    return render(request, 'Vehicle_assignment/service-detail.html')

def car_detail(request):
    return render(request, 'Vehicle_assignment/car-detail.html')

def about(request):
    context = {
        'data':CompanyInfo.objects.all(),
        'about':Abouts.objects.all()
            }
    return render(request, 'Vehicle_assignment/about.html' , context)


def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request , 'Vehicle_assignment/contact.html')
    else:
        form = MessageForm()
    context = {
        'data':CompanyInfo.objects.all(),
        'form':form
            }
    return render(request, 'Vehicle_assignment/contact.html' , context)

def terms(request):
    context = {
        'data':CompanyInfo.objects.all(),
        'terms':Terms.objects.all(),
        'useofterms':UseOfSite.objects.all()
            }
    return render(request, 'Vehicle_assignment/terms.html' , context)

def faq(request):
     context = {
        'data':CompanyInfo.objects.all(),
        'faq':FAQ.objects.all()
            }
     return render(request, 'Vehicle_assignment/faq.html' , context)

def blog(request):
    context = {
        'data':CompanyInfo.objects.all(),
        'blog':Blog.objects.all()
            }
    return render(request, 'Vehicle_assignment/blog-full.html' , context)


def blog_detail(request , pk):
    context = {
        'data':CompanyInfo.objects.all(),
        'blog':Blog.objects.get( id=pk )
            }
    return render(request , 'Vehicle_assignment/blog-single.html' , context)







def login_view(request):
    form = CustomUserLoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            userlogin = authenticate(request, email=username, password=password)
        if userlogin is not None and userlogin.is_superuser:
            login(request, userlogin)
            return redirect('admin_index')
        elif userlogin is not None and userlogin.is_employee:
            login(request, userlogin)
            return redirect('index')
        elif userlogin is not None and userlogin.is_officer:
            login(request, userlogin)
            return redirect('officer')
        else:
            messages.error(request, 'Invalid Password or Email')
    context = {
        'form' : form
    }
    return render(request, 'Vehicle_assignment/login.html', context)




def logout_view(request):
    logout(request)
    return redirect('/')



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed Succesussfuly')
            return redirect('/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'Vehicle_assignment/change_password.html', {'form': form})




@login_required
def employee_review(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    if request.method == 'POST':
        form = EmployeeReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.employee = employee
            review.save()
            return redirect(index)
    else:
        form = EmployeeReviewForm()
    return render(request, 'Vehicle_assignment/employee_review.html', {'form': form, 'employee': employee})

 
def coming_soon(request):
    return render(request, 'Vehicle_assignment/comingsoon.html')

def confirmation(request):
    return render(request, 'Vehicle_assignment/confirmation.html')

def forget_password(request):
    return render(request, 'Vehicle_assignment/forget-password.html')


