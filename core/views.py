from django.shortcuts import render, redirect
from django.contrib.auth import logout

from project.models import Category, Project, Status

from .forms import SignupForm
# Create your views here.
def index(request):
    projects = Project.objects.all()
    categories = Category.objects.all()
    status = Status.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'projects': projects,
        'status': status,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    

    return render(request, 'core/signup.html', {
        'form':form
    })

def logout_view(request):
    logout(request)
    return redirect('core:index')