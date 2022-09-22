from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('createdata',views.createdata,name='createdata'),
    path('updatedata/<str:id>',views.updatedata,name='updatedata'),
    path('deletedata/<str:id>',views.deletedata,name='deletedata')
]
