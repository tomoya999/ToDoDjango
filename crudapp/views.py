from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, ListView, DeleteView

from .forms import TodoForm
from .models import Todo, CustomUser as User
from django.http import HttpResponse

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'todo/index.html'
    login_url = 'users/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = Todo.objects.filter(is_done=False).order_by('updated_at')
        # context['user'] = User.objects.get(pk=self.request.user.pk)
        context['items'] = items
        return context

index = IndexView.as_view()


class DetailsView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todo/detail.html'

class CreateView(LoginRequiredMixin, CreateView):
    model = Todo
    form_class = TodoForm
    template_name ='todo/create.html'
    success_url = "/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class UpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/update.html'
    success_url = "/"

class DeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    success_url = reverse_lazy('crudapp:index')
    template_name = 'todo/delete.html'
