from typing import Optional
from black import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser

from mainapp.permissions import MainAppPermissions, create_permissions


class Command(BaseCommand):
    help = """
    Creates newly added permissions in main app if they don't exist
    """

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--fake",
            action="store_true",
            help="Only returns permissions that would be created",
        )
        return super().add_arguments(parser)

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        fake = options.get("fake", False)
        created_permissions = create_permissions(
            MainAppPermissions.choices, fake=bool(fake)
        )
        faked = "**FAKED**" if fake else ""
        self.stdout.write(
            self.style.SUCCESS(
                f"{faked} Created permissions: {', '.join(created_permissions.keys())}"
                if created_permissions.keys()
                else f"{faked} No new permissions created"
            )
        )
