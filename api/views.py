from .models import InfoCustomer
from .serializers import InfoCustomerSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.contrib.auth.models import User

class InfoCustomerViewSet(viewsets.ModelViewSet):
	serializer_class = InfoCustomerSerializer
	queryset = InfoCustomer.objects.all()
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer