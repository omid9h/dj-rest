from common.services import BaseService
from mainapp.models.customer import Customer


class CustomerService(BaseService):
    """Customer service"""

    def list(self):
        """returns a list of customers"""
        return Customer.objects.all()
