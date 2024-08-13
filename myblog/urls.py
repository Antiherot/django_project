"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from blog_page.views import blog_post, EditPost, CreateCategory,DeletePost
from checklist.views import checklist, edit_entries
from login.views import login_user,logout_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog_post, name='home'),
    path('checklist/',checklist, name='checklist'),
    path('edit_post/<int:pk>/',EditPost.as_view(), name='edit_post'),
    path('delete_post/<int:pk>/',DeletePost.as_view(), name='delete_post'),
    path('checklist/edit_entry/<int:pk>/',edit_entries.as_view(), name='edit_entry'),
    path('create_categories',CreateCategory.as_view(), name='create_categories'),
    path('accounts/login/',login_user, name='login'),
    path('accounts/logout/',logout_user, name='logout'),

    # path('test',quote_view, name='create_categories')

]
