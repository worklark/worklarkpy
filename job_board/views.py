from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.forms import modelform_factory

from .models import JobListing, Employer


def job_listing(request, id):
    job_listing = get_object_or_404(JobListing, pk=id)
    return render(request, "job_board/job_listing.html", {"job_listing": job_listing})


JobListingForm = modelform_factory(JobListing, exclude=[])


def job_listing_new(request):
    form = JobListingForm
    return render(request, "job_board/job_listing_new.html", {"form": form})


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


EmployerForm = modelform_factory(Employer, exclude=[])


def employer_new(request):
    form = EmployerForm
    return render(request, "job_board/employer_new.html", {"form": form})