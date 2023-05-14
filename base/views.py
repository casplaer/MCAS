from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse, FileResponse
from django.contrib.auth.decorators import login_required
from .models import New, User, About, Message, File, Event,\
    Task, UserFiles
from django.contrib.auth import authenticate, login, logout
from .forms import NewForm, RegistrationForm, AboutForm, \
    FileUploadForm, EventCreationForm, TaskCreationForm, \
    FileUUploadForm
from django.shortcuts import get_object_or_404


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
            print("123")
            #messages.error(request, 'Некорректный логин ИЛИ пароль. Проверьте введённые давнные.')


    context = {'page':page}
    return render(request, 'base/login_register.html', context)


def logoutUser(requset):
    logout(requset)
    return redirect('home')


def registerPage(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
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
    files = UserFiles.objects.filter(user=user)
    tasks = Task.objects.filter(groups__in=user.groups.all())
    if request.method == 'POST':
        msg = Message.objects.create(
            user = request.user,
            body=request.POST.get('body')
        )
        return redirect('user-profile', request.user.id)
    context = {'user' : user, 'msgs':msgs, 'tasks':
               tasks, 'files':files}
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
        return render(request, 'base/preview.html', context)


def teachers(request):
    teacher_list = User.objects.filter(status='teacher')
    context = {'teacher_list':teacher_list}
    return render(request, 'base/teacher_list.html', context)


def musicLib(request):
    files = File.objects.all()
    context = {'files':files}
    return render(request, 'base/music_library.html', context)


def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileUploadForm
    context = {'form':form}
    return render(request, 'base/file_upload.html', context)


def file_uupload(request):
    if request.method == 'POST':
        form = FileUUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileUUploadForm
    context = {'form':form}
    return render(request, 'base/file_upload.html', context)


def download_file(request, pk):
    file = get_object_or_404(File, id = pk)
    response = HttpResponse(file.file_upload)
    response['Content-Disposition'] = f'attachment; filename="{file.file_upload.name}"'
    return response


def download_ufile(request, pk):
    file = get_object_or_404(UserFiles, id = pk)
    response = HttpResponse(file.file_upload)
    print(file.file_upload)
    response['Content-Disposition'] = f'attachment; filename="{file.file_upload.name}"'
    return response


def rewards(request):
    info = About.objects.get(id = 1)
    context = {'info':info}
    return render(request, 'base/rewards.html', context)


def teachersInfo(request):
    info = About.objects.get(id = 1)
    context = {'info':info}
    return render(request, 'base/teachers-info.html', context)


def pianoDepartment(request):
    return render(request, 'base/piano_department.html')


def get_piano(request):
    events = Event.objects.filter(department='piano').values('title', 'description', 'date')
    return JsonResponse(list(events), safe=False)


def get_strings(request):
    events = Event.objects.filter(department="strings").values('title', 'description', 'date')
    return JsonResponse(list(events), safe=False)


def get_folk(request):
    events = Event.objects.filter(department="folk").values('title', 'description', 'date')
    return JsonResponse(list(events), safe=False)


def get_string_folk(request):
    events = Event.objects.filter(department="string-folk").values('title', 'description', 'date')
    return JsonResponse(list(events), safe=False)


def get_choir(request):
    events = Event.objects.filter(department="choir").values('title', 'description', 'date')
    return JsonResponse(list(events), safe=False)


def get_theory(request):
    events = Event.objects.filter(department="theory").values('title', 'description', 'date')
    return JsonResponse(list(events), safe=False)


#def get_uni(request, pk):
    # events = Event.objects.filter(department=pk)
    # return JsonResponse(list(events), safe=False)


def new_event(request):
    form = EventCreationForm()
    if request.method == 'POST':
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base/profile.html')

    context = {'form' : form}
    return render(request, 'base/new_event.html', context)


def contingent(request):
    users = User.objects.filter(status='student')
    context = {'users':users}
    return render(request, 'base/contingent.html', context)


def student_info(request, pk):
    student = User.objects.get(id=pk)
    context = {"student": student}
    return render(request, 'base/student_info.html', context)


def diary(request):
    user = request.user
    tasks = Task.objects.all()
    context = {'tasks':tasks}
    return render(request, 'base/diary.html', context)


def homework(request):
    form = TaskCreationForm()
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/homework.html', context)
