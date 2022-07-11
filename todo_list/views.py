from django.shortcuts import render
from django.views import generic

from todo_list.models import Task, Tag


class Index(generic.ListView):
    model = Task
    queryset = Task.objects.all().prefetch_related("tags")
    template_name = "todo_list/index.html"
    context_object_name = "task_list"


class TagListView(generic.ListView):
    model = Tag
    template_name = "todo_list/tag_list.html"
    context_object_name = "tag_list"
