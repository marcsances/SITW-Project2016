"""musicdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login
from django.views.generic import TemplateView
from views import register,completed,profile,perform_logout,loggedout

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='musicapp/index.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^music/', include('musicapp.urls', namespace='musicapp')),
    url(r'^accounts/login', login, name='login'),
    url(r'^accounts/logout$', perform_logout, name='logout'),
    url(r'^accounts/logout/success', loggedout, name='logout_success'),
    url(r'^accounts/register$', register, name='register'),
    url(r'^accounts/register/completed', completed, name='completed'),
    url(r'^accounts/profile', profile, name='profile')
]
