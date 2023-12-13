from django.urls import path

from . import views

# application namespace
app_name = "users"

urlpatterns = [
    # root
    path('', views.home, name='home'),
    # login
    path("login/", views.signin, name="login"),
    # register
    path("register/", views.register, name="register"),
    # logout
    path("logout/", views.signout, name="logout"),
]