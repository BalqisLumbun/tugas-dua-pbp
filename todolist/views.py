from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import todoForm
import datetime
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from todolist.models import toDoList

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data = toDoList.objects.all()
    context = {
        'mytodolist': data,
        'nama': 'Balqis Lumbun/Oka',
        'npm': "2106751184",
        'last_login': request.COOKIES['last_login'],
        
    }
    return render(request, "todolist.html", context)

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