from django.contrib import admin

from .models import JobListing
from .models import Employer

admin.site.register(JobListing)
admin.site.register(Employer)
