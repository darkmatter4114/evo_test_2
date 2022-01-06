"""evo_app URL Configuration

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
from django.urls import path

from evo_app.app.views import get_name, get_full_name, get_all_v2

from evo_app.app.views import index

from evo_app.app.views import get_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name/', get_name, name="name"),
    path('', get_name, name="main"),
    path('all/', get_all),
    path('v2/', get_full_name, name="main2"),
    path('v2/allV2/', get_all_v2,name="v2all"),
]
