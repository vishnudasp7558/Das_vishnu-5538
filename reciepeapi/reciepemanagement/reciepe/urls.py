"""
URL configuration for reciepemanagement project.

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
from django.contrib import admin
from django.urls import path
from reciepe import views


urlpatterns = [
    # path('', views.create,name='create'),
    path('logout/',views.user_logout.as_view()),
    path('createrev/',views.create_rev.as_view()),
    path('revdetail/<int:pk>',views.detail_rev.as_view()),
    path('mealfilter/',views.mealfilter.as_view()),
    path('ingredientfilter/',views.ingredientFilter.as_view()),
    path('cuisinefilter/',views.cuisinefilter.as_view()),
]