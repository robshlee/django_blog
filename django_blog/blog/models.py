from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

blog_categories = (
    ('MACHINE LEARNING', 'Machine Learning'),
    ('RASPBERRY PI', 'Raspberry Pi'),
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