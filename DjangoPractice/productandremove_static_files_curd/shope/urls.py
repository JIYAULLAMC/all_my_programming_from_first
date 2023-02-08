"""shope URL Configuration

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
from urllib import request
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from productapp import views

urlpatterns = [
    path("admin/", admin.site.urls),

# ---------------- pre define class base views ----------

    path("pdcbv/",views.pdcbv.as_view(),name="pdcbv"),
    path("pdcbv/",views.pdcbv.as_view(request,**{'pk':2}),name="pdcbv"),
# ---------------- user define class base views ----------

    # path("udcbv/", views.udcbv.as_view(), name="ucbv"),
    # path("udcbv/<int:pk>/", views.udcbv.as_view(), name="ucbv"),

# ---------------- function base views --------------

    # path("lproduct/",views.lproduct,name="lproduct"),
    # path("createproduct/",views.createproduct,name="createproduct"),
    # path("updateproduct/<int:pk>/",views.updateproduct,name="updateproduct"),
    # path("deleteproduct/<int:pk>/",views.deleteproduct,name="deleteproduct"),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

