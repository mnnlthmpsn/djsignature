from django.urls import path
from .views import index, save_signature

app_name = 'joey'

urlpatterns = [
    path('', index, name='index'),
    path('success/', save_signature, name='save_signature'),
]