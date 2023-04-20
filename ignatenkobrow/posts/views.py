from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import ServiceForm, GroupForm, BlogForm
from .models import Services, Group, Blog


class ServiceList(generic.ListView):
    model = Services
    context_object_name = 'service'


class BlogList(generic.ListView):
    model = Blog
    context_object_name = 'blog'
    form_class = BlogForm
    template_name = 'posts/main_blog.html'


class BlogCreate(generic.CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'posts/blog_creat_form.html'
    success_url = reverse_lazy('blog')


class ServiceChange(generic.UpdateView):
    model = Services
    form_class = ServiceForm
    extra_context = {'title': 'Изменения услуги'}


class ServiceCreate(generic.CreateView):
    model = Services
    form_class = ServiceForm


class CreatGroup(generic.CreateView):
    template_name = 'posts/creat_group.html'
    model = Group
    form_class = GroupForm


def index(request):
    return render(request, 'posts/index.html')

# Create your views here.
