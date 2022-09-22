from dataclasses import field
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList



def show_watchlist(request):
    data = MyWatchList.objects.all()
    stats = count_watch(request)
    context = {
    'watchlist': data,
    'nama': 'Balqis Lumbun -OKA',
    'npm' : '2106751184',
    'status' : stats,
    }
    return render(request, "mywatchlist.html",context)
def count_watch(request):
    data = MyWatchList.objects.count()
    datatrue = MyWatchList.objects.filter(watched="True").count()
    selisih = data - datatrue
    if (datatrue >= selisih):
        return "Selamat, kamu sudah banyak menonton!"
    else:
        return "Wah, kamu masih sedikit menonton!"
        
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json_by_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    # Jika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml_by_id(request,id):
    data = MyWatchList.objects.filter(pk=id)
    # Jika XML
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Create your views here.
