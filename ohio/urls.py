"""ohio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from registry import views as registryviews
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', registryviews.HomeView.as_view()),
    path('api/v1/', registryviews.APIView.as_view()),
    path('api/v1/operators', registryviews.OperatorList.as_view()),
    path('api/v1/operators/<uuid:pk>', registryviews.OperatorDetail.as_view()),
    path('api/v1/operators/<uuid:pk>/privilaged', registryviews.OperatorDetailPrivilaged.as_view()),
    path('api/v1/operators/<uuid:pk>', registryviews.OperatorDetail.as_view()),
    path('api/v1/operators/<uuid:pk>/rpas', registryviews.OperatorRpas.as_view()),
    path('api/v1/rpas/<esn>', registryviews.RpasESNDetails.as_view()),
    path('api/v1/contacts', registryviews.ContactList.as_view()),
    path('api/v1/contacts/<uuid:pk>', registryviews.ContactDetail.as_view()),
    path('api/v1/contacts/<uuid:pk>/privilaged', registryviews.ContactDetailPrivilaged.as_view()),
    path('api/v1/operators/<uuid:pk>/rpas', registryviews.OperatorRpas.as_view()),
    path('api/v1/pilots', registryviews.PilotList.as_view()),
    path('api/v1/pilots/<uuid:pk>', registryviews.PilotDetail.as_view()),
    path('api/v1/pilots/<uuid:pk>/privilaged', registryviews.PilotDetailPrivilaged.as_view()),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = format_suffix_patterns(urlpatterns)