from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import CustomerSerializer


def customers(request):
    # invoke serializer and return to client
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse(
        {"customers": serializer.data}
    )  # This is going to be the json compatible version that we are going to pass as response
