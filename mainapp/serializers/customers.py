from rest_framework import serializers

from mainapp.models.customer import Customer


class CustomerListSerializer(serializers.ModelSerializer):
    """customer list serializer"""

    class Meta:
        model = Customer
        fields = "__all__"
