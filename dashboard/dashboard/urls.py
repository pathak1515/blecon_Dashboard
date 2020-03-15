"""django_adminlte3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from adminpanel.views import redirect_view
from adminpanel import views
from django.apps import apps
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'adminpanel'

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='adminlte/index.html')),
    url(r'^login/$', TemplateView.as_view(template_name='adminlte/login.html')),
    path('admin/', admin.site.urls),
    path('logout/', redirect_view),
    path('admin/myhits/', views.hits, name='myhits'),
    path('admin/department/', views.dept, name='department'),
    path('admin/beacon/', views.bcn, name='beacon')  
] 
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
