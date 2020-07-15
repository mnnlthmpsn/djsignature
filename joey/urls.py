from django.urls import path
from .views import sign, index, view

app_name = 'joey'

urlpatterns = [
    path('', index, name='index'),
    path('sign/', sign, name='sign'),
    path('view/<int:signature_id>/', view, name='view'),
]