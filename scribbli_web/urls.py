"""
URL configuration for scribbli_web project.

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

from scribbli import views as scribbli_views

urlpatterns = [
    # 3rd party urls
    path('admin/', admin.site.urls),

    # Public urls
    path('', scribbli_views.LandingView.as_view(), name='public_landing'),
    path('login/', scribbli_views.LoginView.as_view(), name='public_login'),

    # User urls
    path('home/', scribbli_views.HomeView.as_view(), name='user_home'),

    # Universe urls
    path('universe/', scribbli_views.WorldListView.as_view(), name='universe_world_list'),
    path('universe/world/new/', scribbli_views.WorldCreateView.as_view(), name='universe_world_create'),
    path('universe/world/<int:pk>/', scribbli_views.WorldDetailView.as_view(), name='universe_world_detail'),
    path('universe/world/<int:pk>/edit/', scribbli_views.WorldUpdateView.as_view(), name='universe_world_update'),
    path('universe/world/<int:world_id>/story/new/', scribbli_views.StoryCreateView.as_view(), name='universe_story_create'),

    # Story urls
    path('story/<int:pk>/', scribbli_views.StoryDetailView.as_view(), name='story_detail')
]
