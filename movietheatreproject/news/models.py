from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    cover_image = models.URLField(max_length=500)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.title
