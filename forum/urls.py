from django.urls import path
from .views import ForumListView, ForumDeleteView, ForumDetailView, ForumCreateView, ForumUpdateView

urlpatterns = [
    path("post/<int:pk>/", ForumDetailView.as_view(), name="post_detail"),
    path("", ForumListView.as_view(), name="home"),
    path("post/new/", ForumCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit", ForumUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", ForumDeleteView.as_view(), name="post_delete")
]