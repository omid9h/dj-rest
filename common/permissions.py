from typing import List
from rest_framework import permissions


class CheckIfUserHasPermission(permissions.BasePermission):

    def __init__(self, permission_list: List[str]) -> None:
        self.permission_list = permission_list
        super().__init__()

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.user.has_perms(self.permission_list):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class CheckIfUserIsInAllGroups(permissions.BasePermission):

    def __init__(self, group_list: List[str]) -> None:
        self.group_list = group_list
        super().__init__()

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if set(self.group_list).issubset(list(request.user.groups.values_list('name', flat=True))):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)


class CheckIfUserIsAtLeastInOneGroup(permissions.BasePermission):

    def __init__(self, group_list: List[str]) -> None:
        self.group_list = group_list
        super().__init__()

    edit_methods = ("PUT", "PATCH")

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if set(self.group_list).intersection(list(request.user.groups.values_list('name', flat=True))):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
