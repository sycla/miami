from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("", views.miamibooking, name="miamibooking"),
    path("jetski", views.jetski, name="jetski"),
    path("ponton", views.ponton, name="ponton"),
    path("send-mail", SendMail, name="sendmail"),
    path("servicedetail2",views.miamibooking2, name="miamibooking2"),
    path("servicedetail6/send-mail", SendMail, name="sendmail"),

]
