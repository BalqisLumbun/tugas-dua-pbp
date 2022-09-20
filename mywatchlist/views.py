from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from mywatchlist.models import MyWatchList



def show_watchlist(request):
    data = MyWatchList.objects.all()
    context = {
    'watchlist': data,
    'nama': 'Balqis Lumbun -OKA/2106751184'
    }
    return render(request, "mywatchlist.html",context)
#def count_watch(request):
    #data = MyWatchList.objects.annotate(watched="True")
    #if data 
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
