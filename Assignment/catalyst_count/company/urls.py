from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('upload/', views.upload_data, name='upload_data'),
    path('filter/', views.filter_data, name='filter_data'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('api/companies/', views.CompanyListView.as_view(), name='api_companies'),
    path('clear/', views.clear_database, name='clear_database'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.main, name='main'),

]


