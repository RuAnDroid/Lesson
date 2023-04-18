from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    featured_image = models.ImageField(upload_to='projects/%Y/%m/%d/', default="default.jpg")
    seller = models.CharField(max_length=20)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.title
