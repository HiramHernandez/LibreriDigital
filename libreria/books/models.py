from django.db import models

# Create your models here.


class Book(models.Model):



    name = models.CharField(max_length=30)
    slug = models.SlugField()
    created = models.DateField()
    isbn = models.CharField(max_length=10)
    author = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s %s %s' % (self.name, self.slug, self.created, self.isbn)
