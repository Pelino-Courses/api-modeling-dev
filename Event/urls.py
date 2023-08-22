

# from django.utils import path

from django.urls import path
from Event import views


urlpatterns =[
    path('getall/',views.get_Event),
     path('create/',views.create_Event,name='createEvent'),
]
