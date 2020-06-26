from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Post

def blog_posts(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

class ContactPage(TemplateView):
    template_name = 'blog/contactpage.html'

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

class KobePost(TemplateView):
    template_name = 'blog/kobe_regularization.html'

class MachineLearningBlogPostListView(ListView):
    model = Post
    template_name = 'blog/machine_learning_blog.html' # <app>/<model>_<viewtype>.html
    ordering = ['-date_posted']
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category='MACHINE LEARNING')

        return context

class RaspberryPiBlogPostListView(ListView):
    model = Post
    template_name = 'blog/raspberry_pi_blog.html' # <app>/<model>_<viewtype>.html
    ordering = ['-date_posted']
    paginate_by = 10
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(category='RASPBERRY PI')

        return context

    

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['image', 'title', 'category', 'content']

    def form_valid(self, form): # overriding form_valid method to make author as the requester before running parent class's form_valid method
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form): # overriding form_valid method to make author as the requester before running parent class's form_valid method
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): # makes sure only the author can update his own posts. need to import UserPassesTestMixin
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self): # makes sure only the author can update his own posts. need to import UserPassesTestMixin
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False