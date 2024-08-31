from customers.models import Customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def customers(request):
    """
    List all customers or create a new customer.

    GET: Retrieve a list of all customers.
    POST: Create a new customer.
    """
    if request.method == "GET":
        data = Customer.objects.all()
        serializer = CustomerSerializer(data, many=True)
        return Response({"customers": serializer.data})

    elif request.method == "POST":
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"customer": serializer.data}, status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def customer(request, id):
    """
    Retrieve, update or delete a customer.

    GET: Retrieve a customer by id.
    POST: Update a customer by id.
    DELETE: Delete a customer by id.
    """
    try:
        data = Customer.objects.get(pk=id)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = CustomerSerializer(data)
        return Response({"customer": serializer.data})

    elif request.method == "DELETE":
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == "POST":
        serializer = CustomerSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"customer": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
