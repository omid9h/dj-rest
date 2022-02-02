from django.db.models.query import QuerySet
from common.services import BaseService
from mainapp.models.customer import Customer


class CustomerService(BaseService):
    """Customer service"""

    def list(self) -> QuerySet:
        """returns a list of customers"""
        return Customer.objects.all()
