from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ContactPage, \
    MachineLearningBlogPostListView, DjangoBlogPostListView, ReadingList, ResumeView, BookCreateView, BookDetailView, \
    BookUpdateView, PostDeleteView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', HomePage.as_view(), name='blog-home'),
    path('', PostListView.as_view(), name='blog-posts'),

    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),

    path('book/new', BookCreateView.as_view(), name='book-create'),
    path('book/<int:pk>', BookDetailView.as_view(), name='book-detail'),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name='book-update'),
    path('book/<int:pk>/delete', PostDeleteView.as_view(), name='book-delete'),

    path('about/', views.about, name='blog-about'),
    path('contact/', ContactPage.as_view(), name='contact-page'),
    path('machinelearning/', MachineLearningBlogPostListView.as_view(), name='ml-posts'),
    path('django/', DjangoBlogPostListView.as_view(), name='django-posts'),
    path('readinglist/', ReadingList.as_view(), name='reading-list'),
    path('resume/', ResumeView.as_view(), name='resume-view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
