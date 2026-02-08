from django.urls import path
from . import views

app_name = 'lockerApp'

urlpatterns = [
    path('', views.locker_login_view, name='login'),
    path('verify/', views.locker_verify_view, name='verify'),
    path('dashboard/', views.locker_dashboard_view, name='dashboard'),
]
