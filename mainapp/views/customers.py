from functools import partial
import inject
from common.permissions import CheckIfUserHasPermission
from common.paginations import get_paginated_response, LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from common.views import BaseAPIView
from mainapp.filters import CustomerFilter
from mainapp.permissions import MainAppPermissions
from mainapp.serializers.customers import (
    CustomerCreateSerializer,
    CustomerListSerializer,
)
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


class CustomerCreate(BaseAPIView):
    """create a new customer it doesn't need to handle avatar"""

    permission_classes = (
        IsAuthenticated,
        partial(
            CheckIfUserHasPermission,
            [MainAppPermissions.get_fullname(MainAppPermissions.CUSTOMER_ADMIN)],
        ),
    )
    service = inject.attr(CustomerService)

    def post(self, request):
        serializer = CustomerCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        instance = self.service.create(serializer)

        return Response(
            data={"name": instance.name, "email": instance.email},
            status=status.HTTP_201_CREATED,
        )
