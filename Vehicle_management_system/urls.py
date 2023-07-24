from django.contrib import admin
from django.urls import path , include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sys_admin/', include('Sys_admin.urls')),
    path('', include('Vehicle_assignment.urls')),
]
