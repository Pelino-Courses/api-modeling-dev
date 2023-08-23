

# from django.utils import path

from django.urls import path
from Event import views


urlpatterns =[
    path('getall/',views.get_Event,name="getallEvents"),
    path('create/',views.create_Event,name='createEvent'),
     path('getone/<str:event_id>',views.get_single_event, name="getoneevent" ),
]
