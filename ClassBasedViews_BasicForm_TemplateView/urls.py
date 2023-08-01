"""
URL configuration for ClassBasedViews_BasicForm_TemplateView project.

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
from app.views import *

#-----if we have only a template to render, we can do it directly here in URL patterns by using TemplateView
#-----we dont have to write any view for this 
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('functionBasedView_SF/',functionBasedView_SF,name='functionBasedView_SF'),
    path('ClassBasedView_SF/',ClassBasedView_SF.as_view(),name='ClassBasedView_SF'),
    path('Template_View/',Template_View.as_view(),name='Template_View'),
    
    #-----directly we can specify the template name in url mapping
    path('TemplateView_from_URL/',TemplateView.as_view(template_name='TemplateView_from_URL.html'),name='TemplateView_from_URL'),
]
