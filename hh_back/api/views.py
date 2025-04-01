from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class OneCompany(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class OneVacancy(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

@api_view(['GET'])
def vacancybycompany(request, id):
    vacancy = Vacancy.objects.filter(company_id=id)
    serializer = VacancySerializer(vacancy, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def topvacancy(request):
    vacancy = Vacancy.objects.order_by('-salary')[:10]
    serializer = VacancySerializer(vacancy, many=True)
    return Response(serializer.data)
