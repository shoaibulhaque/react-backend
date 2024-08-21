from rest_framework import serializers
from customers.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer  # Thats the model we want to serialize
        fields = "__all__"
