"""
URL configuration for smarttravels project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('itinerary/', views.itinerary_view, name='itinerary'),
    path('itinerary/<uuid:id>/', views.old_itinerary_view, name='old_itinerary'),
    path('dashboard/', views.clear_itinerary_view, name='clear_itinerary'),
    path('dashboard/<uuid:id>/', views.delete_itinerary_view, name='delete_itinerary'),
    path('contact/', views.contact_view, name='contact'),
    path('', views.home_view, name='home'),
]
