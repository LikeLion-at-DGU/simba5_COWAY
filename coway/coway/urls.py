"""coway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mainpage, name="mainpage"),
    path('/conv', views.convpage, name="convpage"),
    path('/convinfo', views.convinfopage, name="convinfopage"),
    path('/convmap', views.convmappage, name="convmappage"),
    path('/join', views.joinpage, name="joinpage"),
    path('/login', views.loginpage, name="loginpage"),
    path('/ask', views.askpage, name="askpage"),
    path('/edit', views.editpage, name="editpage"),
    path('/home', views.homepage, name="homepage"),
    path('/stpcafe', views.stpcafepage, name="stpcafepage"),
    path('/stpconv', views.stpconvpage, name="stpconvpage"),
    path('/stprest', views.stprestpage, name="stprestpage"),
    path('/stpstd', views.stpstdpage, name="stpstdpage"),
    path('/conv', views.convpage, name="convpage"),
    path('/convinfo', views.convinfopage, name="convinfopage"),
    path('/convmap', views.convmappage, name="convmappage"),
    path('/easyroad', views.easyroadpage, name="easyroadpage"),
    path('/roadchoice', views.roadchoicepage, name="roadchoicepage"),
    path('/shortroad', views.shortroadpage, name="shortroadpage"),
]
