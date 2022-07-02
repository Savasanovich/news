from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):

    title = models.CharField(max_length=30)
    slug = models.SlugField()
    image = models.ImageField(upload_to='static/img')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class About(models.Model):

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/img')
    description = models.TextField()

    def __str__(self):
        return self.title



