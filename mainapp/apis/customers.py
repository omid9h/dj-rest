from functools import partial
import inject
from rest_framework.authentication import TokenAuthentication
from common.permissions import CheckIfUserHasPermission
from common.paginations import get_paginated_response, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from common.views import BaseAPIView
from mainapp.filters import CustomerFilter
from mainapp.permissions import CustomerPermissions
from mainapp.serializers.customers import CustomerListSerializer
from mainapp.services.customer import CustomerService


class CustomerList(BaseAPIView):
    """returns a list of customers"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        IsAuthenticated,
        partial(CheckIfUserHasPermission, [CustomerPermissions.ADMIN.value]),
    )
    service = inject.attr(CustomerService)
    filterset_class = CustomerFilter

    def get(self, request):
        return get_paginated_response(
            pagination_class=LimitOffsetPagination,
            serializer_class=CustomerListSerializer,
            queryset=self.filtered_queryset(request.GET, self.service.list()),
            request=request,
            view=self,
        )
