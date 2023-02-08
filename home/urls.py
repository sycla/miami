from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    path('miamiabout', views.miamiabout, name='miamiabout'),
    path('miamiservices', views.miamiservices, name='miamiservices'),
    path('miamiboats', views.miamiboats, name='miamiboats'),
    path('miamicontact', views.miamicontact, name='miamicontact'),
    path('servicedetail1', views.servicedetail1, name='servicedetail1'),
    path('servicedetail2', views.servicedetail2, name='servicedetail2'),
    path('servicedetail3', views.servicedetail3, name='servicedetail3'),
    path('servicedetail4', views.servicedetail4, name='servicedetail4'),
    path('servicedetail5', views.servicedetail5, name='servicedetail5'),
    path('servicedetail6', views.servicedetail6, name='servicedetail6'),

]
