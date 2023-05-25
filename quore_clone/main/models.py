from django.db import models
from django.contrib.auth.admin import User
from django.utils.text import slugify

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.SlugField(max_length=1000,default="")
    date = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Answer(models.Model):
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return f"{self.question}"