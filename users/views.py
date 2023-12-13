
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group, Permission
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import requests


def signin(request):
    # Displays the login form and signs a user in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login user in it exists and redirect to the home page
            login(request, user)
            return HttpResponseRedirect(reverse('users:home'))
        else:
            return render(request, "users/login.html", {
                "messages": ["Invalid username or password"],
            })
    return render(request, "users/login.html")


def register(request):
    # Displays a registration form. Creates a user and signs them in
    if request.method == "POST":
        # Create a group if needed and adds the user to the group with permissions to edit tasks
        group, created = Group.objects.get_or_create(name="standard_user")
        try:
            user = User.objects.create_user(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                email=request.POST["email"],
                username=request.POST["username"],
                password=request.POST["password"]
            )
            user.groups.add(group)
            login(request, user)
            return HttpResponseRedirect(reverse('users:home'))
        except Exception as exc:
            return render(request, "users/register.html", {
                "messages": ["That username already exists"],
                "first_name": request.POST["first_name"],
                "last_name": request.POST["last_name"],
                "email": request.POST["email"],
                "username": request.POST["username"],
                "password": request.POST["password"],
            })
    return render(request, "users/register.html")


def signout(request):
    # Log out user and redirect to home
    logout(request)
    return HttpResponseRedirect(reverse('users:home'))

# display home page
def home(request):
    context = {}
    query = request.GET.get('q', None)
    if query is not None:
        context['data'] = get_api_data(query)
    return render(request, 'home.html',context)


# send GET request to spotify API and get data
# need to input your own key for spotify api
def get_api_data(query):
   url = "https://spotify23.p.rapidapi.com/search/"
   querystring = {"q":query,"type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}
   headers = {
       "X-RapidAPI-Key": "insert key",
       "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
   }
   response = requests.get(url, headers=headers, params=querystring)
   return response.json()