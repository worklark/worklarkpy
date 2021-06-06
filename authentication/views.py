from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout

# Create your views here.


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "" or password == "":
            return HttpResponse("Missing username or password!")
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("Unauthorized!")
        return HttpResponse(f"Your username is: {request.user.username}")
    else:
        return render(request, "authentication/login.html")


def logout_user(request):
    logout(request)
    return HttpResponse("Successfully logged out!")