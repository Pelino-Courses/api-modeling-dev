from django.urls import path
from . import views

urlpatterns = [
    path('', views.participants),
    path('<int:id>', views.get_participant),
    ]