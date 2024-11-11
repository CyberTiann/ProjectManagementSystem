from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Category, Status, Year
from .forms import NewProjectForm, EditProjectForm
# Create your views here.
# project = item, 

def projects(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    year_id = request.GET.get('year', 0)
    
    categories = Category.objects.all()
    years = Year.objects.all()
    projects = Project.objects.all()

    if category_id:
        projects = projects.filter(category_id=category_id)
    
    if year_id:
        projects = projects.filter(year_id=year_id)
    
    if query:
        projects = projects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(started__icontains=query) 
        )

    # Calculate total cost
    total_cost = 0
    for project in projects:
        # Remove ₱ symbol and any commas, then convert to float
        try:
            cost = float(project.project_cost.replace('₱', '').replace(',', '').strip())
            total_cost += cost
        except (ValueError, AttributeError):
            continue

    # Format total cost with commas
    formatted_total_cost = "{:,.2f}".format(total_cost)

    return render(request, 'project/projects.html',{
        'projects': projects,
        'query': query,
        'categories': categories,
        'years': years,
        'category_id': int(category_id),
        'year_id': int(year_id),
        'total_cost': formatted_total_cost
    })

@login_required
def detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.filter(category=project.category).exclude(pk=pk)[0:3]
    
    return render(request, "project/detail.html",{
        'project': project,
        'related_projects': related_projects
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)

        if form.is_valid():
            project = form.save(commit=False)
            project.uploader = request.user
            project.save()

            return redirect('project:detail', pk=project.id)
        else:
            form = NewProjectForm()
    form = NewProjectForm()

    return render(request, 'project/form.html',{
        'form': form,
        'title': 'New Project'
    })
@login_required
def edit(request,pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = EditProjectForm(request.POST, request.FILES, instance=project)

        if form.is_valid():
            form.save()

            return redirect('project:detail', pk=project.id)
    else:
        form = EditProjectForm(instance=project)

    return render(request, 'project/form.html',{
        'form': form,
        'title': 'Edit Project'
    })

@login_required
def delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()

    return redirect('/')