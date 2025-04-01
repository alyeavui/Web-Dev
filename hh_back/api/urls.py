from django.urls import path
from .views import CompanyList, OneCompany, VacancyList, OneVacancy, vacancybycompany, topvacancy

urlpatterns = [
    path('companies/', CompanyList.as_view(), name='companylist'),
    path('companies/<int:pk>/', OneCompany.as_view(), name='onecompany'), 
    path('companies/<int:id>/vacancies/', vacancybycompany, name='vacancyincompany'),
    path('vacancies/', VacancyList.as_view(), name='vacancylist'),
    path('vacancies/<int:pk>/', OneVacancy.as_view(), name='onevacancy'), 
    path('vacancies/top_ten/', topvacancy, name='topvacancy'),
]
