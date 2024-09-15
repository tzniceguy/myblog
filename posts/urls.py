from django.urls import path
from .views import PostList,PostDetail

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<slug:slug>/', PostDetail.as_view())
]
