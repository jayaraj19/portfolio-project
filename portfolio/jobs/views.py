from django.shortcuts import render
from jobs.models import Job, Certificate


# Create your views here.
def index(request):
    jobs = Job.objects
    certificates = Certificate.objects
    return render(request, 'jobs/base.html', {'jobs': jobs, 'certificates': certificates})

# def works(request):
#     jobs = Job.objects
#     return render(request, 'jobs/works.html', {'jobs': jobs})
#
#
# def certificate(request):
#     certificates = Certificate.objects
#     return render(request, 'jobs/certificates.html', {'certificates': certificates})
