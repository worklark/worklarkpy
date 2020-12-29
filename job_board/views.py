from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import JobListing, Employer


def job_listing(request, id):
    job_listing = get_object_or_404(JobListing, pk=id)
    return render(request, "job_board/job_listing.html", {"job_listing": job_listing})


def job_listings(request):
    job_listings = get_list_or_404(JobListing)
    return render(
        request, "job_board/job_listings.html", {"job_listings": job_listings}
    )


def employer(request, id):
    employer = get_object_or_404(Employer, pk=id)
    return render(request, "job_board/employer.html", {"employer": employer})


def employers(request):
    employers = get_list_or_404(Employer)
    return render(request, "job_board/employers.html", {"employers": employers})