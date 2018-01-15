from django.core import serializers
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
import datetime
import json

# Create your views here.
from django.views.decorators.http import require_http_methods

from webapi.models import Book


@require_http_methods(["GET", "POST"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.POST.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods('GET')
def show_books(request):
    # response = {}
    # try:
    #     books = Book.objects.all()
    #     print("haha")
    #     response['list'] = json.loads(serializers.serialize("json", books))
    #     response['msg'] = 'success'
    #     response['error_num'] = 0
    # except Exception as e:
    #     response['msg'] = str(e)
    #     response['error_num'] = 1
    # return JsonResponse(response)


    # all_objs = Book.objects.all()
    # all_dicts = todicts(all_objs)
    # all_jsons = json.dumps(all_dicts,cls=CJsonEncoder, ensure_ascii=False)
    # return HttpResponse(all_jsons)

    all_objs = Book.objects.all()
    status = 0
    result = "success"
    return HttpResponse(json.dumps({
        "status": status,
        "result": result,
        "datalist":[{
            "id":obj.id,
            "book_name":obj.book_name,
            "created_time":obj.created_time
        }for obj in all_objs]
    },cls=CJsonEncoder, ensure_ascii=False))



class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)