from django.contrib import admin
from .models import Company

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'country', 'total_employee_estimate')
    search_fields = ('name', 'industry', 'country')
    list_filter = ('industry', 'country')
