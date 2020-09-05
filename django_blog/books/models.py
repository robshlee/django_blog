from django.db import models

read_choices = (
    ('READING', 'Reading'),
    ('TO_READ', 'To Read'),
    ('FINISHED_READING', 'Finished Reading')
)

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    read_stage = models.CharField(choices=read_choices, max_length=100)
    comment = models.TextField()
    rating = models.ChoiceField(choices=[1,2,3,4,5], max_length=10)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})