"""
URL configuration for webove_stranky project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# erneks_project/urls.py
from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('poptat/', views.poptat_dopravu, name='poptat'),
    path('o_nas/', views.o_nas, name='o_nas'),
    path('nabidka_dopravy/', views.nabidka_dopravy, name='nabidka_dopravy'),
    path('volna-mista/', views.jobs_list, name='jobs_list'),
    path('apply/', views.apply, name='apply'),
]