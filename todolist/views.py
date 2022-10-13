from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from todolist.forms import todoForm
import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.core import serializers
from todolist.models import toDoList
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = toDoList.objects.filter(user=request.user)
    context = {
        'mytodolist': data,
        'nama': 'Balqis Lumbun/Oka',
        'npm': "2106751184",
        'uname':username_in(request),
        'last_login': request.COOKIES['last_login'],
        
    }
    return render(request, "todolist.html", context)

def username_in(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
        return username

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
# @csrf_exempt
def new_list(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        finished = False
        addtask = toDoList(date=datetime.date.today(),user=user,title=title,description=description,finished=finished)
        addtask.save()
        return redirect('todolist:show_todolist')
    return render(request, "newtodo.html")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def finish_task(request, pk):
    lists=toDoList.objects.get(id=pk)
    if lists.finished == True:
        lists.finished = False            
    else:
        lists.finished = True
    lists.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
@csrf_exempt
def delete_task(request, pk):
    lists=toDoList.objects.get(id=pk)
    lists.delete()
    return redirect('todolist:show_todolist')

def json(request):
    data = toDoList.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        finished = False

        new_to_do_list = toDoList( date=datetime.date.today(), title=title, description=description, user=user, finished=finished)
        new_to_do_list.save()

        return JsonResponse(
            {"pk" : new_to_do_list.pk, 
            "fields": {
            "date" : new_to_do_list.date,
            "title" : new_to_do_list.title,
            "description" : new_to_do_list.description,
            "is_finished" : new_to_do_list.finished,
        }})

    return HttpResponseNotFound()