# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse

# Create your views here.
from newapp.models import User


def UserDetails(request):
    user_data = User.objects.prefetch_related('activityperiod').values('id', 'tz', 'real_name'
                                                                       , 'activityperiod__start_time',
                                                                       'activityperiod__end_time').order_by('id')
    resp = []
    id_list = {}
    for user in user_data:
        if user['id'] not in id_list:
            item = {}
            activity = {}
            activity_list = []
            activity["start_time"] = user["activityperiod__start_time"]
            activity["end_time"] = user["activityperiod__end_time"]
            activity_list.append(activity)
            item["id"] = user['id']
            item["real_name"] = user["real_name"]
            item["tz"] = user["tz"]
            item["activity_periods"] = activity_list
            resp.append(item)
        else:
            activity = {}
            pre_activity = item["activity_periods"]
            activity["start_time"] = user["activityperiod__start_time"],
            activity["end_time"] = user["activityperiod__end_time"]
            pre_activity.append(activity)
            item["activity_periods"] = pre_activity
    result = {}
    result["ok"] = 'true'
    result["members"] = resp
    return JsonResponse(result)
