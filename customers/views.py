from customers.models import Customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def customers(request):
    # invoke serializer and return to client
    if request.method == "GET":
        data = Customer.objects.all()
        serializer = CustomerSerializer(data, many=True)
        return Response(
            {"customers": serializer.data}
        )  # This is going to be the json compatible version that we are going to pass as response
    elif request.method == "POST":
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"customer": serializer.data}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Function to get a single customer
@api_view(["GET", "POST", "DELETE"])  # which methods we can use
def customer(request, id):
    try:
        data = Customer.objects.get(pk=id)  # searching with id
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CustomerSerializer(data)
        return Response(
            {"customer": serializer.data}
        )  # This is going to be the json compatible version that we are going to pass as response

    elif request.method == "DELETE":
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "POST":
        serializer = CustomerSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"customer": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
