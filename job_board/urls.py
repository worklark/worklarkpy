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
from django.urls import path
from job_board import views

urlpatterns = [
    path("job_listings/<int:id>", views.job_listing, name="job_listing"),
    path("job_listings/new", views.job_listing_new, name="job_listings_new"),
    path("job_listings/", views.job_listings, name="job_listings"),
    path("employers/<int:id>", views.employer, name="employer"),
    path("employers/new", views.employer_new, name="employers_new"),
    path("employers/", views.employers, name="employers"),
]
