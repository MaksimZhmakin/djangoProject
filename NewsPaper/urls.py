"""NewsPaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from news_paper.views import News, New, FilterNews, PostDeleteView, PostUpdateView, PostAddView 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', News.as_view(), name='news'),
    path('news/<int:pk>', New.as_view(), name='new'),
    path('news/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('news/<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('news/add/', PostAddView.as_view(), name='add'),
    path('news/search/', FilterNews.as_view(), name='search'),
    
]