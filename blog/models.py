from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name





class City(models.Model):
    title = models.CharField(max_length=212)
    description = models.TextField()
    language = models.CharField(max_length=212)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title