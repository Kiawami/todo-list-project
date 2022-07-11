from django.urls import path

from todo_list.views import Index, TagListView

urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list")
]
