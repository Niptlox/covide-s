from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.statistic_ru, name='ru'),
    path('reg', views.statistic_reg, name='reg'),
    path('world', views.statistic_world, name='world'),
    # path('map/ru', views.map_ru, name='mapRU'),
    # path('world?country=<str>', views.statistic_world, name='world_'),

]
