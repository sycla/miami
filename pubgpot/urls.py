"""pubgpot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as user_views
from miamihome import views

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('profile/', user_views.profile, name='profile'),
    path('accounts/', include('accounts.urls')),
    path('matchregis/', include('matchregis.urls')),
    path('miamibooking/', include('miamibooking.urls')),
    path('miamihome/', views.index, name="index"),
    path('miamiabout/', views.miamiabout, name="miamiabout"),
    path('miamiservices/', views.miamiservices, name="miamiservices"),
    path('miamiboats/', views.miamiboats, name="miamiboats"),
    path('miamicontact/', views.miamicontact, name="miamicontact"),
    path('servicedetail1/', views.miamibooking, name="servicedetail1"),
    path('servicedetail2/', views.miamibooking2, name="servicedetail2"),
    path('servicedetail3/', views.miamibooking3, name="servicedetail3"),
    path('servicedetail4/', views.miamibooking4, name="servicedetail4"),
    path('servicedetail5/', views.miamibooking5, name="servicedetail5"),
    path('servicedetail6/', views.miamibooking6, name="servicedetail6"),
    path("send-mail", views.SendMail, name="sendmail"),
    path("insta-login", views.InstaLogin, name="instalogin"),
    path("servicedetail2/send-mail", views.SendMail, name="sendmail"),
    path("servicedetail3/send-mail", views.SendMail, name="sendmail"),
    path("servicedetail4/send-mail", views.SendMail, name="sendmail"),
    path("servicedetail5/send-mail", views.SendMail, name="sendmail"),
    path("servicedetail6/send-mail", views.SendMail, name="sendmail"),

    # -----------------
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),


]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  