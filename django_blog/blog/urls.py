from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, ContactPage, \
    MachineLearningBlogPostListView, RaspberryPiBlogPostListView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', HomePage.as_view(), name='blog-home'),
    path('', PostListView.as_view(), name='blog-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('contact/', ContactPage.as_view(), name='contact-page'),
    path('machinelearning/', MachineLearningBlogPostListView.as_view(), name='ml-posts'),
    path('raspberrypi/', RaspberryPiBlogPostListView.as_view(), name='rpi-posts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
