from django.urls import path
from .views import *
urlpatterns = [
    path('',registerpage),
    path('first/',firstpage),
     path('regi/',registerpage),
     path('login/',loginpage),
      path('sports/',sportscar),
      path('coupe/',coupecar),
      path('sedan/',sedancar),
      path('wagon/',wagoncar),
      path('suv/',xuvcar),
      path('carregi/',carregister),
      path('details/<int:id>',detailspage,name='detailspage'),
      path('addwish/<int:itemid>',addwish),
       path('wishdisplay/',wishdisplay),
       path('wishdelete/<int:cartid>',wishdelete),
]