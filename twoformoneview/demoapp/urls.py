from django.urls import path

from demoapp import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'), # AJAX

]