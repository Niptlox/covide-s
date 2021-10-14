from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.statistic_ru, name='ru'),
    path('world', views.statistic_world, name='world'),

]