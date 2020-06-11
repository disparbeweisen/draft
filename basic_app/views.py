from django.shortcuts import render
from basic_app.models import Company, Jobs

def index(request):
    jobs_list = Jobs.objects.order_by('job_name')
    job_dict = {'jobs': jobs_list}
    return render(request, "basic_app/index.html", context = job_dict)
# Create your views here.


# Create your views here.
