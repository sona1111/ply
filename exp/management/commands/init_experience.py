from django.core.management.base import BaseCommand, CommandError

from bs4 import BeautifulSoup
import uuid
from ply import system_uuids,settings
from django.contrib.auth.models import User
import os

from dynapages.models import Templates,Page,Widget,PageWidget
from community.models import Community
from profiles.models import Profile
from exp.models import Level

class Command(BaseCommand):
    help = 'Creates the Base level: Level 1 in all communities: THIS SHOULD ONLY BE DONE ONCE PER SETUP!'


    def handle(self, *args, **options):
        # All profiles must be owned by the primary admin:
        comms = Community.objects.filter(archived=False,frozen=False)
        for community in comms:
        # Create the magic Profile in the System:
            self.stdout.write(self.style.SUCCESS(f"Creating Level 0 in Community: '{community.name}'...."))
            clevel = Level.objects.get_or_create(community=community,level=0,expr=-1)[0]
            clevel.save()
            self.stdout.write(self.style.SUCCESS(f"Creating Level 1 in Community: '{community.name}'...."))
            clevel = Level.objects.get_or_create(community=community,level=1,expr=0)[0]
            clevel.save()
        self.stdout.write(self.style.SUCCESS('Success!'))

