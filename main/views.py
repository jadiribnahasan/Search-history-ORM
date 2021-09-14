import json
from django.shortcuts import render
from .models import Search
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
import datetime

# Create your views here.


def index(request):

    objects = Search.objects.all()

    keywords = []
    users = []

    for item in objects.iterator():
        keywords.append(item.keyword)
        users.append(item.user)

    keywordcount = {}
    for key in keywords:
        count = Search.objects.filter(keyword=key).count()
        keywordcount[key] = count

    userCount = {}
    for user in users:
        count = Search.objects.filter(user=user).count()
        userCount[user] = count

    context = {
        'keywords': keywords,
        'keyCount': keywordcount,
        'users': users,
        'userCount': userCount
    }

    return render(request, "main/index.html", context=context)


def filter(request):
    if request.method == 'GET' and request.is_ajax:

        userchecked = request.GET.get('userUnchecked', None)
        keywordchecked = request.GET.get('keywordUnchecked', None)
        others = request.GET.get('others', None)
        dateRange = request.GET.get('dateRange', None)

        keywordchecked = json.loads(keywordchecked)
        userchecked = json.loads(userchecked)
        dateRange = json.loads(dateRange)

        objects = Search.objects.all()

        obj = None
        if(len(userchecked) == 0 and len(keywordchecked) == 0):
            obj = Search.objects.none()

        else:
            obj = Search.objects.none()

            if len(userchecked) != 0:
                for item in userchecked:
                    obj = obj | objects.filter(user=item)

            if len(keywordchecked) != 0:
                for item in keywordchecked:
                    obj = obj | objects.filter(keyword=item)

        if 'yesterday' in others:
            yesterday = datetime.datetime.today() - datetime.timedelta(days=1)
            obj = obj | objects.filter(time__gte=yesterday)

        if 'lastweek' in others:
            one_week_ago = datetime.datetime.today() - datetime.timedelta(weeks=1)
            obj = obj | objects.filter(time__gte=one_week_ago)

        if 'lastmonth' in others:
            one_month_ago = datetime.datetime.today() - datetime.timedelta(days=30)
            obj = obj | objects.filter(time__gte=one_month_ago)

        if dateRange['start'] and dateRange['end']:
            obj = obj | objects.filter(
                time__range=[dateRange['start'], dateRange['end']])

        # serializing the obj queryset into json format
        obj = serializers.serialize('json', obj)

        return JsonResponse({"res": obj}, status=200)
    else:
        return HttpResponse("Request method is not a GET")
