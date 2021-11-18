from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    choice = (
        ('gastronomy', 'Gastronomy'),
        ('science', 'Science'),
        ('anime', 'Anime'),
        ('education', 'Education'),
        ('social', 'Social'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    category = models.CharField(max_length=50, choices=choice, default="gastronomy")
    image = models.ImageField(upload_to="media/%Y/%m/%d", blank=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique_for_date='created')
    body = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('journal:detail', args=[self.category,self.slug])


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)