import json
import argparse

from django.core.management.base import BaseCommand

from ...services import searcher

class Command(BaseCommand):
    help = "Import the calendar names form a package_mapping.json"

    def add_arguments(self, parser):
        parser.add_argument(
            "--website",
            default="https://www.odata.org.il"
        )
        parser.add_argument(
            "--query",
            default="name:יומן"
        )
        parser.add_argument(
            "--force",
            action="store_true",
            help="Update a matching calendar if found",
        )

    def handle(self, *args, **options):
        searcher.process_resources(
            query=options['query'],
            website=options['website'],
            force=options['force'],
        )

