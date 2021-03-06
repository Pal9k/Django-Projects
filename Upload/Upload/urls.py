"""Upload URL Configuration

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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Image_Gallary1 import views

from django.conf.urls.static import static
from django.conf import settings

from Image_Gallary2 import urls
from Image_Gallary1 import urls
from PPT_Gallary import urls
from Document_Gallary import urls
from demo import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('Image_Gallary/',include('Image_Gallary1.urls')),
    path('Image_Gallary/',include('Image_Gallary2.urls')),
    path('PPT_Gallary/',include('PPT_Gallary.urls')),
    path('Document_Gallary/',include('Document_Gallary.urls')),
    path('demo/',include('demo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
