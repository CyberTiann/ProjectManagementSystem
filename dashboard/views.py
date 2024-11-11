from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from project.models import Project

@login_required
def index(request):
    projects = Project.objects.all()

    return render(request, 'dashboard/index.html',{
        'projects': projects
    })
# Create your views here.

