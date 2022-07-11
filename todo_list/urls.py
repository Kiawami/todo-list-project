from django.urls import path

from todo_list.views import Index, TagListView, TaskCreateView, TagCreateView, TaskDeleteView, TagDeleteView, \
    TaskUpdateView, TagUpdateView, change_status

urlpatterns = [
    path("", Index.as_view(),
         name="index"),
    path("tags/", TagListView.as_view(),
         name="tag-list"),
    path("tasks/create", TaskCreateView.as_view(),
         name="task-create"),
    path("tag/create", TagCreateView.as_view(),
         name="tag-create"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(),
         name="task-delete"),
    path("tag/<int:pk>/delete/", TagDeleteView.as_view(),
         name="tag-delete"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(),
         name="task-update"),
    path("tag/<int:pk>/update/", TagUpdateView.as_view(),
         name="tag-update"),
    path("task/<int:pk>/change_status/", change_status,
         name="change-status"),
]
