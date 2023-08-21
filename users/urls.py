from django.urls import path, include
from .views import *

# url for our users app

urlpatterns = [
    path('register', register.as_view()),
    path('login', login.as_view()),
    path('user/<str:JWTUser>', userView.as_view()),
    path('logout', logout.as_view()),
    
]