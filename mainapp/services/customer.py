from django.db.models.query import QuerySet
from common.services import BaseService
from mainapp.models.customer import Customer
from mainapp.serializers.customers import CustomerCreateSerializer


class CustomerService(BaseService):
    """Customer service"""

    def list(self) -> QuerySet:
        """returns a list of customers"""
        return Customer.objects.all()

    def create(self, serializer: CustomerCreateSerializer) -> Customer:
        """create a new customer it doesn't need to handle avatar"""
        return Customer.objects.create(**serializer.validated_data)
