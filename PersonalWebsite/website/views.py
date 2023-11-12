from django.shortcuts import render
from website.models import Project, Work

# Create your views here.
#connects front end of website to django framework

def cover(request):
    return render(request, 'cover.html', {} )

def about(request):
    return render(request, 'about.html', {})

def project_index(request):
    #gets all the projects in the data base
    projects = Project.objects.all()
    url = str(Project.image).replace('static', '')
    #context dictionary to connect latest projects to website
    context = {
        'projects': projects, 'url': url
    }
    return render(request, 'project_index.html', context)

def work(request):
    #gets all the work history in the data base
    works = Work.objects.all
    url = str(Project.image).replace('static', '')
    #context dictionary to connect latest work history to website
    context = {
        'works': works, 'url': url
    }
    return render(request, 'work.html', context)

def resume(request):
    return render(request, 'resume.html', {})

