from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Book

class ReadingList(TemplateView):
    template_name = 'blog/reading_list.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title','subtitle','author','read_stage','comment']

    def form_valid(self, form): # overriding form_valid method to make author as the requester before running parent class's form_valid method
        form.instance.author = self.request.user
        return super().form_valid(form)

class BookDetailView(DetailView):
    model = Book

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title','subtitle','author','read_stage','comment']

    def form_valid(self, form): # overriding form_valid method to make author as the requester before running parent class's form_valid method
        form.instance.author = self.request.user
        return super().form_valid(form)


# class BookDeleteView(LoginRequiredMixin, DeleteView):
#     model = Book
#     success_url = '/'
