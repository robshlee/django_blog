from django.urls import path
from .views import BookCreateView, BookDetailView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('book/new', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete', PostDeleteView.as_view(), name='book-delete'),
]

