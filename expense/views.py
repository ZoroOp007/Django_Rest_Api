from django.shortcuts import render
from .models import Transaction
from rest_framework.response import Response
from .serializers import TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Sum

# Create your views here.


## This is a example of creating view using decorator called @api_view
@api_view()
def get_transaction(request):
    queryset = Transaction.objects.all()
    serializer = TransactionSerializer(queryset,many=True)
    return Response({
        'data' : serializer.data,
    })



## This is the use of APIView Class to create a API

class TransactionAPI (APIView):
    def get(self, request):
        queryset = Transaction.objects.all().order_by('-id')
        serializer = TransactionSerializer(queryset,many=True)

        return Response({
                "data" : serializer.data,
                "total" : queryset.aggregate(Sum("amount"))
            }, status= status.HTTP_200_OK)
          

    def post(self, request):

        data = request.data
        serializer = TransactionSerializer(data = data)

        if not serializer.is_valid():

            return Response({
                "message" : "data not saved",
                "error" : serializer.errors,
            })

        serializer.save()

        return Response({
            'data' : serializer.data,
            "message" : "data saved "
        })

    def put(self, request):

        data = request.data

        if not data.get("id"):
            return Response({
                "message" : "data not updated",
                "error" : "id is required"
            })
        
        transaction = Transaction.objects.get( id = data.get("id"))

        serializer = TransactionSerializer(transaction,data=data,partial=False)

        if not serializer.is_valid():

            return Response({
                "message" : "data not updated",
                "errors" : serializer.errors
            })
        
        serializer.save()

        return Response({
            "message" : "data updated",
            "data" : serializer.data
        })


    def patch(self,request):

        data = request.data

        if not data.get("id"):
            return Response({
                "message" : "data not updated",
                "errors" : "id is required"
            })
        
        transaction = Transaction.objects.get(id = data.get("id"))

        serializer = TransactionSerializer(transaction,data = data, partial=True)

        if not serializer.is_valid():
            return Response ({
                "message" : "data not saved",
                "errors" : serializer.errors,
            })
        
        serializer.save()

        return Response({
            "message" : "data saved",
            "data" : serializer.data,
        })

    def delete(self,request):

        data = request.data

        if not data.get('id'):
            return Response({
                "message" : "data not deleted",
                "error" : "id is required"
            })
        
        transaction = Transaction.objects.get(id=data.get('id')).delete()

        return Response({
            "message" : "data deleted",
            "data" : {}
        })
        
