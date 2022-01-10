from django.db import models
# from django.contrib.postgres.fields import ArrayField


class Theatre(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=500)
    # show_times = ArrayField(models.TimeField(
    #     null=False, blank=False), blank=False)

    def __str__(self):
        return self.name
