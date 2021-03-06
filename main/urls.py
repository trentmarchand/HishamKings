"""hishamkings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.login_request, name='login'),
    path('homepage/', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('sportsbook/', views.sportsbookpage, name='sportsbook'),
    path('account/', views.paymentEntry, name='account'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('update_bet/<str:pk>/', views.updateBet, name='update_bet'),
    path('delete_bet/<str:pk>/', views.deleteBet, name='delete_bet'),
    path('analytics/', views.analytics, name='analytics'),
    path('add_bet/', views.add_bet, name='add_bet'),
]
