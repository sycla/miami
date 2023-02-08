from django.urls import path
from . import views

urlpatterns = [
    path("", views.matchregis, name="matchregis"),
    path("duomatchregis", views.duomatchregis, name="duomatchregis"),
    path("squadmatchregis", views.squadmatchregis, name="squadmatchregis"),

]
