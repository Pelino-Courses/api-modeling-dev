

# from django.utils import path

from django.urls import path
from Event import views


urlpatterns =[
    path('getall/',views.get_Event,name="getallEvents"),
    path('getallcategory/',views.get_Category,name="getallCategory"),
    path('create/',views.create_Event,name='createEvent'),
    path('createCategory/',views.create_Category,name='createCategory'),
    path('getone/<str:event_id>',views.get_single_event, name="getoneevent" ),
    path('delete/<str:pk>',views.EventDelete, name="deleteevent" ),
    path('update/<str:event_id>',views.update_single_event, name="getoneeventand_update" ),
]
