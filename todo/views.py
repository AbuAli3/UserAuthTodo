from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, TodoForm
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.utils import timezone

def home(request):
    return render(request, 'home.html')

# User views
def userRegister(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home page if user is already authenticated

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home page if user is already authenticated

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')  # Set error message
    return render(request, 'accounts/login.html')

def userLogout(request):
    logout(request)
    return redirect('home')

# Todo views
@login_required(login_url='login')
def todoList(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created')
    return render(request, 'todo/home.html', {'todos': todos})

@login_required(login_url='login')
def delTodo(request, item_id):
    todo = get_object_or_404(Todo, pk=item_id)
    todo.delete()
    return redirect('home')

@login_required(login_url='login')
def addTodo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Assign the currently logged-in user as the owner of the todo
            if not todo.created:
                todo.created = timezone.now()
            todo.save()
            return redirect('home')
    else:
        form = TodoForm()

    context = {'form': form}
    return render(request, 'todo/add_todo.html', context)
