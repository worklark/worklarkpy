from django.db import models


class Employer(models.Model):
    """The employers that employ employees"""

    operating_name = models.CharField(max_length=200, null=False, blank=False)
    registered_name = models.CharField(max_length=200, default="")
    shortname = models.CharField(max_length=200, null=False, blank=False, unique=True)
    website = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.operating_name}"


class JobListing(models.Model):
    """The listings that contain individual job specifications"""

    title = models.CharField(max_length=254)
    description = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} @ {self.employer.operating_name}"
