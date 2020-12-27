from django.db import models


class Employer(models.Model):
    """The employers that employees"""

    name = models.CharField(max_length=254)

    def __str__(self):
        return f"{self.name}"


class JobListing(models.Model):
    """The listings that contain individual job specifications"""

    title = models.CharField(max_length=254)
    description = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} @ {self.employer.name}"
