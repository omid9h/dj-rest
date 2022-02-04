from __future__ import annotations
from typing import List, Tuple, TypedDict
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import TextChoices

from mainapp.models.permission import Access

app_name = "mainapp"


class MainAppPermissions(TextChoices):
    """
    holds all permissions for the mainapp
    """

    CUSTOMER_ADMIN = "customer_admin", "Customer Admin"

    @staticmethod
    def get_fullname(permission: MainAppPermissions) -> str:
        return f"{app_name}.{permission.value}"


class PermissionsDict(TypedDict):
    """
    TypedDict for permissions
    """

    codename: str
    permission: Permission


def create_permissions(mainapp_permissions: List[Tuple[str, str]]) -> PermissionsDict:
    """
    Create permissions for the app
    and returns a dict with the permissions created
    """
    permissions_dict = {}
    content_type = ContentType.objects.get_for_model(Access)

    for codename, name in mainapp_permissions:
        if not Permission.objects.filter(
            codename=codename, content_type=content_type
        ).exists():
            permission = Permission.objects.create(
                codename=codename,
                name=name,
                content_type=content_type,
            )
            permissions_dict[codename] = permission

    return permissions_dict
