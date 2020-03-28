from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import TodoForm
from .models import Todo
from django.http import HttpResponse

class IndexView(LoginRequiredMixin, generic.ListView):
    model =Todo
    # paginate_by = 10
    ordering = ['updated_at']
    template_name = 'todo/index.html'
    login_url = 'users/login/'


class DetailsView(generic.DetailView):
    model = Todo
    template_name = 'todo/detail.html'

class CreateView(generic.edit.CreateView):
    model = Todo
    form_class = TodoForm
    template_name ='todo/create.html'
    success_url = "/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

class UpdateView(generic.edit.UpdateView):
    model = Todo
    fields = '__all__'
    template_name = 'todo/update.html'
    success_url = "/"

class DeleteView(generic.edit.DeleteView):
    model = Todo
    success_url = reverse_lazy('crudapp:index')
    template_name = 'todo/delete.html'
