from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='cv'),
    path('details/<int:id>', views.details, name='details'),
    
]
