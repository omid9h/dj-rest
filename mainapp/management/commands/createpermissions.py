from typing import Optional
from black import Any
from django.core.management.base import BaseCommand

from mainapp.permissions import MainAppPermissions, create_permissions


class Command(BaseCommand):
    help = """
    create newly added permissions in main app if they don't exist
    """

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        created_permissions = create_permissions(MainAppPermissions.choices)
        self.stdout.write(
            self.style.SUCCESS(
                f"created permissions: {', '.join(created_permissions.keys())}"
                if created_permissions.keys()
                else "no new permissions created"
            )
        )
