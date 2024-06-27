from django.core.management.base import BaseCommand
from scribbli.models import User


class Command(BaseCommand):
    help = 'Create some users for testing / local development.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Create normal user
        pleb = User.objects.create_user('pleb', 'pleb@test.com', 'pleb001')

        # Create moderator
        mod = User.objects.create_user('mod', 'mod@test.com', 'mod001')

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created the following users: {pleb}, {mod}')
        )
