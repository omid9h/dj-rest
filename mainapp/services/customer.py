from django.db.models.query import QuerySet
from common.services import BaseService
from mainapp.models.customer import Customer
from mainapp.serializers.customers import (
    CustomerCreateSerializer,
    CustomerUploadAvatarSerializer,
)


class CustomerService(BaseService):
    """Customer service"""

    def list(self) -> QuerySet:
        """returns a list of customers"""
        return Customer.objects.all()

    def create(self, serializer: CustomerCreateSerializer) -> Customer:
        """create a new customer it doesn't need to handle avatar"""
        return Customer.objects.create(**serializer.validated_data)

    def upload_avatar(self, serializer: CustomerUploadAvatarSerializer) -> Customer:
        """upload avatar for a customer via id"""
        try:
            customer = Customer.objects.get(id=serializer.validated_data["customer_id"])
        except Customer.DoesNotExist:
            raise ValueError("Customer does not exist")
        customer.avatar = serializer.validated_data["avatar"]
        customer.save()
        return customer
