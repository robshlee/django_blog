from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

blog_categories = (
    ('MACHINE LEARNING', 'Machine Learning'),
    ('DJANGO', 'Django'),
)

read_choices = (
    ('READ', 'Read'),
    ('TO_READ', 'To Read'),
    ('READING', 'Reading')
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=blog_categories, null=True)
    image = models.ImageField(default='default.png', upload_to='thumbnails')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    read_stage = models.CharField(choices=read_choices, max_length=100)
    comment = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})