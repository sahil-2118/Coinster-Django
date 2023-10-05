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
from scheduler.views import (SchedulerDetail,
                             SchedulerList,
                             SchedulerRequest,
                             )
from user.views import (LoginView, 
                        ListCreateView, 
                        RetrieveUpdateDestroyView,
                        LogoutView,
                        )
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# ... the rest of your URLconf goes here ...




schema_view = get_schema_view(
   openapi.Info(
      title="Coinster API",
      default_version='v1',
      description="Coinster description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/cryptos/', CryptoList.as_view()),
    path('v1/cryptos/<pk>', CryptoDetail.as_view(), name="crypto_detail"),
    path('v1/schedulers/', SchedulerList.as_view()),
    path('v1/scheduler/<pk>/', SchedulerDetail.as_view()),
    path('v1/scheduler/', SchedulerRequest.as_view()), 
    path('v1/login/', LoginView.as_view()),
    path('v1/logout/', LogoutView.as_view()),
    path('v1/users/', ListCreateView.as_view()),
    path('v1/user/<pk>/', RetrieveUpdateDestroyView.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)