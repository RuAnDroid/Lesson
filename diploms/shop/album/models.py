from django.db import models


class Card(models.Model):
    seller = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, blank=True)
    featured_image = models.ImageField(upload_to='projects/%Y/%m/%d/', default="default.jpg")
    price = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
