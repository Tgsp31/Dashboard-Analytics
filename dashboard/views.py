

# Create your views here.
from rest_framework import viewsets
from .models import DataPoint
from .serializers import DataPointSerializer
from django.shortcuts import render

class DataPointViewSet(viewsets.ModelViewSet):
    queryset = DataPoint.objects.all()
    serializer_class = DataPointSerializer


def index(request):
    return render(request, "index.html")
