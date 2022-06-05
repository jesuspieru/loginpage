from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.paginator import Paginator
from requests import request

from .models import task

class customloginview(LoginView):
    template_name = 'loginapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class registerpage(FormView):
    template_name = 'loginapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(registerpage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(registerpage, self).get(*args, **kwargs)




class tasklist(ListView):
    model = task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            context['tasks'] = context['tasks'].filter(user=self.request.user)
            context['count'] = context['tasks'].filter(complete=False).count()

            search_input = self.request.GET.get('search-area') or ""
            if search_input:
                context['tasks'] = context['tasks'].filter(title__icontains=search_input)
                context['search_input'] = search_input

            tareas = context['tasks'].order_by('id')
            page = self.request.GET.get('page',1)
            try:
                paginator = Paginator(tareas,10)
                context['tasks'] = paginator.page(page)
            except:
                raise Http404
            
        else:
            context['tasks'] = task.objects.all().order_by('id')
          

            search_input = self.request.GET.get('search-area') or ""
            if search_input:
                context['tasks'] = context['tasks'].filter(title__icontains=search_input)
                context['search_input'] = search_input
                 
            tareas = context['tasks'].order_by('id')
            page = self.request.GET.get('page',1)
            try:
                paginator = Paginator(tareas,10)
                context['tasks'] = paginator.page(page)
            except:
                raise Http404

        return context

class taskdetail( DetailView):
    model = task
    context_object_name = 'task-detail'
    template_name = 'loginapp/task.html'

class taskcreate(LoginRequiredMixin, CreateView):
    model = task
    fields = ['title','picture', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(taskcreate, self).form_valid(form)
    
class taskupdate(LoginRequiredMixin, UpdateView):
    model = task
    fields = ['title','picture', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class taskdelete(LoginRequiredMixin, DeleteView):
    model = task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')