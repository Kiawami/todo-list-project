from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from todo_list.forms import TaskForm
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


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "todo_list/create_task.html"
    success_url = reverse_lazy("todo_list:index")
    form_class = TaskForm


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "todo_list/create_tag.html"
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo_list/delete_task.html"
    success_url = reverse_lazy("todo_list:index")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo_list/delete_tag.html"
    success_url = reverse_lazy("todo_list:tag-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    template_name = "todo_list/create_task.html"
    success_url = reverse_lazy("todo_list:index")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    template_name = "todo_list/create_tag.html"
    success_url = reverse_lazy("todo_list:tag-list")


def change_status(request, pk):
    current_task = Task.objects.get(id=pk)
    current_task.is_done = not current_task.is_done
    current_task.save()
    return HttpResponseRedirect(reverse_lazy("todo_list:index"))
