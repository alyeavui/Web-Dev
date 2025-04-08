from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.companies, name='companies'),
    path('companies/<int:id>/', views.onecompany, name='one-company'),
    path('companies/<int:id>/vacancies/', views.vacanciesInCompany, name='vacancies-in-company'),
    path('vacancies/', views.Vacancies.as_view(), name='vacancies'),
    path('vacancies/<int:id>/', views.OneVacancy.as_view(), name='one-vacancy'),
    path('vacancies/top_ten/', views.TopVacancies.as_view(), name='top-vacancies'),
]