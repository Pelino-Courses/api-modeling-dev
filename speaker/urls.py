from django.urls import path
from . import views

urlpatterns = [
    path('', views.speakers),
    path('<int:id>', views.get_speaker),
    ]