from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('check_result/<str:result_id>', views.check_result, name = 'check_result'),
]
