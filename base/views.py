from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import New, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import NewForm, RegistrationForm

# Create your views here.
def home(request):
    news = New.objects.order_by('-created')[:3]
    context = {'news':news}
    return render(request, 'base/home.html', context)

def new(request, pk):
    new = New.objects.get(id=pk)
    count = New.objects.count()
    context = {'new': new, 'count':count}
    return render(request, 'base/news.html', context)

def loginPage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, "Такого пользователя не существует")
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Некорректный логин ИЛИ пароль. Проверьте введённые давнные.')


    context = {'page':page}
    return render(request, 'base/login_register.html', context)

def logoutUser(requset):
    logout(requset)
    return redirect('home')

def registerPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Во время регистрации возникла ошибка')

    return render(request, 'base/login_register.html', {'form' : form})

@login_required(login_url='/login')
def userProfile(request, pk):
    user = User.objects.get(id = pk)
    context = {'user' : user}
    return render(request, 'base/profile.html', context)

@login_required(login_url = "/login")
def createNew(request):
    form = NewForm()
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, 'base/new_form.html', context)

def newsPage(request):
    news = New.objects.order_by('-created')
    context = {'news' : news}
    return render(request, 'base/article_list.html', context)

def deleteNew(request, pk):
    new = New.objects.get(id=pk)
    new.delete()
    return redirect('news')

def editNew(request, pk):
    new = New.objects.get(id = pk)
    form = NewForm()
    if request.method == 'POST':
        form = NewForm(request.POST, instance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewForm(instance=new)

    context = {'new':new, 'form':form}
    return render(request, 'base/edit-new.html', context)