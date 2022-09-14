from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_item_katalog = CatalogItem.objects.all()
    context = {
        'list_katalog': data_item_katalog,
        'nama': 'Balqis A. Lumbun',
        'npm': '2106751184'
    }
    return render(request, "katalog.html",context)

# TODO: Create your views here.
