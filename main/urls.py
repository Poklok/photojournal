from django.urls import path

from main.views import PostListView, PostDetailView, blog_post_like

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post-like/<int:pk>', blog_post_like, name="post_like"),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail')
]
