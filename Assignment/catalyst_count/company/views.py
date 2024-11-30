from .forms import UploadFileForm
from .models import Company
from .forms import FilterForm
from rest_framework.generics import ListAPIView
from .models import Company
from .serializers import CompanySerializer
import csv
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from company.models import Company
from django.contrib.auth.models import User
from django.contrib.auth import login


@login_required
def upload_data(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']

            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
                csv_reader = csv.reader(decoded_file)
                headers = next(csv_reader, None)
                print(f"Headers: {headers}")
                batch = []
                for i, row in enumerate(csv_reader):
                    try:
                        batch.append(Company(
                            name=row[1],
                            domain=row[2],
                            year_founded=int(row[3]) if row[3] else None,
                            industry=row[4],
                            size_range=row[5],
                            locality=row[6],
                            country=row[7],
                            linkedin_url=row[8],
                            current_employee_estimate=int(row[9]) if row[9] else None, 
                            total_employee_estimate=int(row[10]) if row[10] else None,
                        ))
                        if len(batch) >= 1000:
                            Company.objects.bulk_create(batch)
                            print(f"Inserted {len(batch)} rows into the database")
                            batch = []

                    except Exception as row_error:
                        print(f"Error processing row {i}: {row}, Error: {row_error}")
                if batch:
                    Company.objects.bulk_create(batch)
                    print(f"Inserted remaining {len(batch)} rows into the database")
                return redirect('filter_data')

            except Exception as e:
                return render(request, 'upload.html', {'form': form, 'error': f"Error parsing file: {e}"})
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


@login_required
def filter_data(request):
    form = FilterForm(request.GET)
    companies = Company.objects.all()
    print(companies.query)
    if form.is_valid():
        if form.cleaned_data.get('name'):
            companies = companies.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data.get('industry'):
            companies = companies.filter(industry__icontains=form.cleaned_data['industry'])
        if form.cleaned_data.get('country'):
            companies = companies.filter(country__icontains=form.cleaned_data['country'])

    return render(request, 'filter.html', {'form': form, 'companies': companies, 'count': companies.count()})


class CompanyListView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

def clear_database(request):
    Company.objects.all().delete()
    return redirect('/company/filter/') 

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, password=password)

        login(request, user)
        return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def main(request):
    return render(request,'main.html')