from customers.models import Customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerializer


def customers(request):
    # invoke serializer and return to client
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse(
        {"customers": serializer.data}
    )  # This is going to be the json compatible version that we are going to pass as response


# Function to get a single customer
def customer(request, id):
    try:
        data = Customer.objects.get(pk=id)  # searching with id
    except Customer.DoesNotExist:
        raise Http404("Customer does not exist")
    serializer = CustomerSerializer(data)
    return JsonResponse(
        {"customer": serializer.data}
    )  # This is going to be the json compatible version that we are going to pass as response
