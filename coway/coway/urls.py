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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.videopage, name="videopage"),
    path('main/', views.mainpage, name="mainpage"),
    
    path('conv/', views.convpage, name="convpage"),
    path('cafemap/', views.cafeMappage, name="cafeMappage"),
    path('convmap/', views.convMappage, name="convMappage"),
    path('stdmap/', views.stdMappage, name="stdMappage"),
    path('restmap/', views.restMappage, name="restMappage"),
    
    path('join/', views.joinpage, name="joinpage"),
    path('login/', views.loginpage, name="loginpage"),
    path('logout/', views.logout, name="logout"),
    
    path('ask/', views.askpage, name="askpage"),
    path('create/', views.create, name="create"),
    
    path('edit/', views.editpage, name="editpage"),
    path('home/', views.homepage, name="homepage"),
    
    path('easyroad/', views.easyroadpage, name="easyroadpage"),
    path('roadchoice/', views.roadchoicepage, name="roadchoicepage"),
    path('shortroad/', views.shortroadpage, name="shortroadpage"),

    path('bookmark/', views.bookmarkpage, name="bookmarkpage"),
    path('deletebookmark/<int:id>', views.deletebookmark, name="deletebookmark"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)