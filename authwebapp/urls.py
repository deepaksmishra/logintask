"""deepakmtask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from authwebapp import views
from django.urls import path, re_path
from authwebapp.views import home
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='main-view'),
    path('login',views.login1,name='login'),
    path('fileupload',views.fileupload,name='fileupload'),
    path('showdata',views.showdata,name='showdata'),

]


#+ static(settings.media, document_root=settings.MEDIA_ROOT)