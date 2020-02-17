from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import Customer
from .serializers import CustomerSerializers
# Create your views here.


class get_delete_update_customer(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializers

    def get_queryset(self, pk):
        try:
            customers = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            content = {
                'status': 'Not Found'
            }
            return Response(content, status=status.HTTP_400_NOT_FOUND)
        return customers

    # Get the perticuler data
    def get(self, request, pk):
        customer = self.get_queryset(pk)
        serializer = CustomerSerializers(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update the data
    def put(self, request, pk):
        customer = self.get_queryset(pk)
        serializer = CustomerSerializers(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            content = {
                'message': 'Data Updated'
            }
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete Data
    def delete(self, request, pk):
        customer = self.get_queryset(pk)
        customer.delete()
        content = {
            'message': 'Data deleted'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)


class get_post_customers(ListCreateAPIView):
    serializer_class = CustomerSerializers

    def get_queryset(self):
        customer = Customer.objects.all()
        return customer

    # Get all Customer

    def get(self, request):
        customer = self.get_queryset()
        serializer = CustomerSerializers(customer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {'message': 'Customer Created'}
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
