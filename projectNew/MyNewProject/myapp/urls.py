from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='list_view'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
