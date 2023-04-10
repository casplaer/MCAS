from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import New, User, About, Message
from django.contrib.auth import authenticate, login, logout
from .forms import NewForm, RegistrationForm, AboutForm

# Create your views here.
def home(request):
    news = New.objects.order_by('-created')[:3]
    about = About.objects.get(id = 1)
    context = {'news':news, 'about':about}
    return render(request, 'base/home.html', context)

def new(request, pk):
    new = New.objects.get(id=pk)
    prev = New.objects.filter(id__lt=pk).last()
    next = New.objects.filter(id__gt=pk).first()
    prev_new = New.objects.filter(id__lt=pk).order_by('-id').first()
    next_new = New.objects.filter(id__gt=pk).order_by('id').first()
    context = {'new': new, 'prev':prev, 'next':next, 'prev_new':prev_new, 'next_new':next_new}
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
    msgs = user.message_set.all().order_by('-created')
    context = {'user' : user, 'msgs':msgs}
    return render(request, 'base/profile.html', context)

@login_required(login_url = "/login")
def createNew(request):
    form = NewForm()
    if request.method == 'POST':
        form = NewForm(request.POST)
        if 'preview' in request.POST:
            if form.is_valid():
                title = form.cleaned_data.get('title')
                description = form.cleaned_data.get('description')
                context = {'title':title, 'description':description}
                return render(request, 'base/preview.html', context)
        elif 'publish' in request.POST:
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

def about(request):
    about = About.objects.get(id = 1)
    context = {'about':about}
    return render(request, 'base/about.html', context)

def editAbout(request):
    about = About.objects.get(id=1)
    form = AboutForm()
    if request.method == 'POST':
        form = AboutForm(request.POST, instance=about)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AboutForm(instance=about)

    context = {'about':about, 'form':form}

    return render(request, 'base/edit-about.html', context)

def preview(request):
    if request.method == 'GET':
        form_data = request.POST
        context = {'form_data':form_data}
        return render(request, 'preview.html', context)