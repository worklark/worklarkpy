from django.urls import path
from django.urls.conf import include
from authentication import views

urlpatterns = [
    path("login/", views.login_user),
    path('accounts/', include('django.contrib.auth.urls')),
]
