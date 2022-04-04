from django.urls import path

from main.views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list')
]
