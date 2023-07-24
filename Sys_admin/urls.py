from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.admin_index, name='admin_index'),

      path('form_employee/' , views.register_view_emoloyee , name ='form_employee'),

        path('form_officer/' , views.register_view_officer , name ='form_officer'),

          path('form_driver/' , views.register_view_driver , name ='form_driver'),

             path('form_vehicle/' , views.register_view_vehicle , name ='form_vehicle'),

                path('Edit_Company_Info/<int:pk>' , views.edit_company_info , name='form_Company_info'),

                  path('Edit_slider/<int:pk>' , views.edit_slider , name='edit_slider'),
                   
                    path('Add_serice/' , views.add_service , name='add_service'),

                       path('officer/' , views.officer , name='officer'),
  
                           path('edit_registry/<str:pk>/', views.edit_registry, name='edit_registry'),
                
                                path('inbox/', views.inbox_view, name='inbox_view'),
              
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)