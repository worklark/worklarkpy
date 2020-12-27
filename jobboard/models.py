from django.db import models


class JobListing(models.Model):
    title = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"