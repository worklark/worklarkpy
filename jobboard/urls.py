"""worklark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import job_listing, job_listings, employer, employers

urlpatterns = [
    path("job_listings/<int:id>", job_listing, name="job_listing"),
    path("job_listings/", job_listings, name="job_listings"),
    path("employers/<int:id>", employer, name="employer"),
    path("employers/", employers, name="employers"),
]
