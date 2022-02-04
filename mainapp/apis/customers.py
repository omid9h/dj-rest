from functools import partial
import inject
from common.permissions import CheckIfUserHasPermission
from common.paginations import get_paginated_response, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from common.views import BaseAPIView
from mainapp.filters import CustomerFilter
from mainapp.permissions import MainAppPermissions
from mainapp.serializers.customers import CustomerListSerializer
from mainapp.services.customer import CustomerService


class CustomerList(BaseAPIView):
    """returns a list of customers"""

    permission_classes = (
        IsAuthenticated,
        partial(
            CheckIfUserHasPermission,
            [MainAppPermissions.get_fullname(MainAppPermissions.CUSTOMER_ADMIN)],
        ),
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
