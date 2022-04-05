from django.urls import path

from main.views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>', PostDetailView.as_view(), name='post_detail')
]
