from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('about', views.about, name='about'),
    # path('miamiabout', views.about, name='miamiabout'),
    # path('miamiabout', views.miamiabout, name='miamiabout'),
]
