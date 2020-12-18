from django.core.management.base import BaseCommand
from django.utils import timezone
from dojo.models import Finding

"""
Author: tohch4
This script will generate a substantial amount of test data, beyond the sample
data fixtures you can optionally for improved load and performance testing.
"""


class Command(BaseCommand):
    help = 'findings_count: number of desired findings to insert into database'

    def add_arguments(self, parser):
        parser.add_argument('findings_count')

    def handle(self, *args, **options):
        findings_count = options['findings_count']
        self.create_product()
        self.create_engagement()
        self.generate_test_data()

    def create_product():
        pass

    def create_engagement():
        pass

    def generate_test_data():
        pass