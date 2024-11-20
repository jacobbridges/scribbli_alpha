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

from scribbli import views as sv

urlpatterns = [
    # 3rd party urls
    path('admin/', admin.site.urls),

    # Public urls
    path('', sv.LandingView.as_view(), name='public_landing'),
    path('login/', sv.LoginView.as_view(), name='public_login'),

    # My (current user specific) urls
    path('my/home/', sv.HomeView.as_view(), name='my_home'),
    path('my/p/characters-select/', sv.MyPartialCharacterListView.as_view(purpose='select'), name='my_p_characters_select'),

    # My actionable urls
    path('logout/', sv.LogoutView.as_view(), name='logout'),

    # Universe urls
    path('universe/', sv.WorldListView.as_view(), name='universe_world_list'),
    path('universe/world/new/', sv.WorldCreateView.as_view(), name='universe_world_create'),
    path('universe/world/<int:pk>/', sv.WorldDetailView.as_view(), name='universe_world_detail'),
    path('universe/world/<int:pk>/edit/', sv.WorldUpdateView.as_view(), name='universe_world_update'),
    path('universe/world/<int:pk>/story/new/', sv.StoryCreateView.as_view(), name='universe_story_create'),
    path('universe/world/<int:pk>/stories/', sv.WorldStoryListView.as_view(), name='universe_world_story_list'),
    path('universe/world/<int:pk>/character/new/', sv.CharacterCreateView.as_view(), name='universe_character_create'),
    path('universe/world/<int:pk>/natives/', sv.WorldCharacterListView.as_view(leaf='natives'), name='universe_world_native_list'),
    path('universe/world/<int:pk>/residents/', sv.WorldCharacterListView.as_view(leaf='residents'), name='universe_world_resident_list'),
    path('universe/character/<int:pk>/', sv.CharacterDetailView.as_view(), name='universe_character_detail'),
    path('universe/character/<int:pk>/edit/', sv.CharacterUpdateView.as_view(), name='universe_character_update'),

    # Story urls
    path('story/<int:pk>/', sv.StoryDetailView.as_view(), name='story_detail'),
    path('story/<int:pk>/edit/', sv.StoryUpdateView.as_view(), name='story_update'),
    path('story/<int:pk>/join_request/new/', sv.StoryJoinRequestSubmitView.as_view(), name='story_join_request_submit'),
    path('story/<int:pk>/join-requests/', sv.StoryJoinRequestList.as_view(), name='story_join_request_list'),
    path('story/<int:pk>/join-request/resolve/', sv.StoryJoinRequestResolveView.as_view(), name='story_join_request_resolve'),
]
