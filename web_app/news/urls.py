from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create/', views.news_create, name='news_create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='update-detail'),
    path('<int:pk>/delete', views.NewsDeleteView.as_view(), name='delete-detail'),
]
