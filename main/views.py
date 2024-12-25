from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import *


class ContactCreateView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

