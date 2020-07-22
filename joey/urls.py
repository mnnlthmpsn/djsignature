from django.urls import path
from .views import index, save_signature, submit_questionnaire

app_name = 'joey'

urlpatterns = [
    path('', index, name='index'),
    path('success/', save_signature, name='save_signature'),
    path('submit/', submit_questionnaire, name='submit')
]