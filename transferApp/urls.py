from django.urls import path
from . import views

app_name = 'transferApp'

urlpatterns = [
    path('send/', views.send_view, name='send'),
    path('receive/', views.receive_view, name='receive'),
    path('r/<str:code>/', views.receive_direct_view, name='receive_direct'),
]
