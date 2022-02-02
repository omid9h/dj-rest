from django_filters import (
    FilterSet,
    NumberFilter,
    DateFromToRangeFilter,
    ModelMultipleChoiceFilter,
    CharFilter,
)

from mainapp.models.customer import Customer


class CustomerFilter(FilterSet):
    postpone_after = NumberFilter(field_name="postpone_date", lookup_expr="gt")

    class Meta:
        model = Customer
        fields = {
            key: ["exact", "contains"]
            for key in (
                "name",
                "email",
            )
        }
