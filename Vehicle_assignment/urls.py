from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name='index'),

     path('car_detail/', views.car_detail, name='car_detail'),

      path('service/', views.service, name='service'), 

        path('contact/', views.contact, name='contact'),

         path('terms/', views.terms, name='terms'),

          path('faq/', views.faq, name='faq'),

           path('blog/', views.blog, name='blog'),

            path('blog/<int:pk>/',views.blog_detail, name='blog_detail'),
            
             path('coming_soon/', views.coming_soon, name='coming_soon'),

              path('confirmation/', views.confirmation, name='confirmation'),

               path('forget_password/', views.forget_password, name='forget_password'),
                     
                path('login/', views.login_view, name='login'),

                 path('logout/', views.logout_view, name='logout'),
    
                  path('about/', views.about, name='about'),

                    path('add_registry/', views.add_registry, name='add_registry'),

                      path('change_password/', views.change_password, name='change_password'),
                        
                          path('employees/<int:employee_id>/review/', views.employee_review, name='employee_review'),

                            path('end_trip/', views.end_trip, name='end_trip'),

              
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)