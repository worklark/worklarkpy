from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import JobListing

# Create your views here.


def detail(request, id):
    job_listing = get_object_or_404(JobListing, pk=id)
    return render(request, "jobboard/detail.html", {"job_listing": job_listing})


def job_listings(request):
    job_listings = get_list_or_404(JobListing)
    return render(request, "jobboard/job_listings.html", {"job_listings": job_listings})