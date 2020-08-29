"""ghost_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from ghost_app import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('upvote/<int:post_id>/', views.upvote_view),
    path('downvote/<int:post_id>/', views.downvote_view, name="downvote"),
    path('roast/', views.roast_post, name="roast"),
    path('boast/', views.boast_post, name="boast"),
    path('sorted/', views.sorted_post, name="sorted"),
    path('post/', views.create_post, name="post"),
    path('admin/', admin.site.urls),
]
