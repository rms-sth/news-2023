from django.urls import path

from blog_app import views

app_name = "news-admin"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", views.PostDetailView.as_view(), name="post-detail"),
    path("post-delete/<int:pk>/", views.PostDeleteView.as_view(), name="post-delete"),
    path("post-create/", views.PostCreateView.as_view(), name="post-create"),
    path("post-update/<int:pk>/", views.PostUpdateView.as_view(), name="post-update"),
    path("draft-list", views.DraftListView.as_view(), name="draft-list"),
    path("draft-detail/<int:pk>/", views.DraftDetailView.as_view(), name="draft-detail"),
    path("draft-publish/<int:pk>/", views.DraftPublishView.as_view(), name="draft-publish"),
    path("draft-delete/<int:pk>/", views.DraftDeleteView.as_view(), name="draft-delete"),
]
