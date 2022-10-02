from django.core.management.base import BaseCommand,CommandError
from .models import Story
from datetime import datedelta,timedelta

class Command(BaseCommand):
    help('Deleting the data older then 10 days')
    def handle(self,*args,**options):
        Story.objects.filter(story_time_stamp__lte=datetime.now()-timedelta(seconds=60))