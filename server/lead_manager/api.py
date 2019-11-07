from .models import UserModel, SalesLeadModel, CompanyModel
from rest_framework import viewsets, permissions
from .serializers import SalesLeadModelSerializer, CompanyModelSerializer, UserModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class SalesLeadViewSet(viewsets.ModelViewSet):
    queryset = SalesLeadModel.objects.all()
    serializer_class = SalesLeadModelSerializer
    permission_classes = [
        permissions.AllowAny
    ]

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanyModelSerializer
    permission_classes = [
        permissions.AllowAny
    ]
