import json
from datetime import datetime

from dateutil import parser
from django.core.management.base import BaseCommand
from newapp.models import User, ActivityPeriod


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('test.json') as f:
            data_list = json.load(f)
        activity = []
        for data in data_list['members']:
            activity.append(data['activity_periods'])
        user_obj = [
            User(
                id=item['id'],
                real_name=item['real_name'],
                tz=item['tz']
            )
            for item in data_list['members']
        ]
        User.objects.bulk_create(objs=user_obj)
        activity_obj = [
            ActivityPeriod(
                fk=user_obj[activity.index(item)],
                start_time=parser.parse(val['start_time']),
                end_time=parser.parse(val['end_time'])
            )
            for item in activity for val in item
        ]
        ActivityPeriod.objects.bulk_create(objs=activity_obj)
