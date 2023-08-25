from typing import Any
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_categories_fixture.json")
        call_command("loaddata", "db_admin_user_fixture.json")
        call_command("loaddata", "db_brands_fixture.json")
        call_command("loaddata", "db_colors_fixture.json")
        call_command("loaddata", "db_products_fixture.json")
        call_command("loaddata", "db_camera_features_fixture.json")
        call_command("loaddata", "db_communication_standarts_fixture.json")
        call_command("loaddata", "db_smartphones_fixture.json")
