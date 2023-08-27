"""
URL configuration for coinster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from cryptocurrency.views import CryptoList, CryptoDetail
from scheduler.views import SchedulerDetail,SchedulerList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/cryptos/', CryptoList.as_view()),
    path('v1/cryptos/<pk>', CryptoDetail.as_view()),
    path('v1/schedulers/', SchedulerList.as_view()),
    path('v1/scheduler/<pk>/', SchedulerDetail.as_view()), 
]
