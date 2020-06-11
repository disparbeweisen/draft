import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Kotlin.settings")

import django
django.setup()

import random
from faker import Faker
from basic_app.models import Company, Jobs

fakegen = Faker()

companies = ["Google", "Facebook", "Amazon", "Microsoft", "Apple"]

def add_company():
    t = Company.objects.get_or_create(company_name = random.choice(companies))[0]
    t.save()
    return t

def populate(N = 5):

    for entry in range(N):
        #get the topic for the entry
        company = add_company()

        #create the fake data for that entry
        fake_name = fakegen.job()
        fake_url = fakegen.url()

        #create the new job entry
        work = Jobs.objects.get_or_create(company_topic = company, job_name = fake_name, more_info = fake_url)[0]

if __name__ == '__main__':
    print("populate")
    populate(10)
    print("populating complete")
