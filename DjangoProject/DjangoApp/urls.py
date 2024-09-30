
from django.urls import path
from . import views
from .views import all_django, details

urlpatterns = [
    
    path('',views.all_django, name='all_django'),
    path('<int:Django_id>/', views.details, name='Django_details'),
    path('clg_loc/', views.college_loc, name='Clg_Location'),
    
]
