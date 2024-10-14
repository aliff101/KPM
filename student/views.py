from django.shortcuts import render
from student.models import course as CourseModel
from student.models import Mentor 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    return render (request,"index.html")

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code'] 
        c_desc = request.POST['desc']
        data = CourseModel(code=c_code, desc=c_desc) 
        data.save()
        message = 'Data Saved Successfully'
    else:
        message =''

    courses = CourseModel.objects.all().values()

    context = {
        'message': message,
        'courses': courses,
    }

    return render(request, "course.html", context)

def mentor(request):
    if request.method == 'POST':
        m_id = request.POST['id'] 
        m_name = request.POST['name']
        m_room = request.POST['room']
        data = Mentor(id=m_id,name=m_name,room=m_room) 
        data.save()
        message = 'Data Saved Successfully'
    else:
        message = ''
    
    mentors = Mentor.objects.all().values()

    context = {
        'message':message,
        'mentors':mentors,
    }

    return render(request, "newmentor.html", context)

def update_course(request,code):
    data=CourseModel.objects.get(code=code)
    dict = {
        'code':code
    }
    return render (request,'update_course.html',dict)

def save_update_course(request,code):
    c_desc = request.POST['desc']
    data=CourseModel.objects.get(code=code)
    data.desc = c_desc
    data.save()
    return HttpResponseRedirect(reverse('Course'))

def update_mentor(request,id):
    data=Mentor.objects.get(id=id)
    dict = {
        'id':id
    }
    return render (request,'update_mentor.html',dict)

def save_update_mentor(request,id):
    c_room = request.POST['desc']
    data=Mentor.objects.get(id=id)
    data.room = c_room
    data.save()
    return HttpResponseRedirect(reverse('mentor'))

def delete_course(request,code):
    data = CourseModel.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('Course'))

def delete_mentor(request,id):
    data = Mentor.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse('mentor'))

def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')
        
        if c_code:
            data = CourseModel.objects.filter(code=c_code.upper())
        else:
            data = None

        context = {
            'data': data
        }

        return render(request, 'search_course.html', context)
    
def search_mentor(request):
    if request.method == 'GET':
        c_code = request.GET.get('i_id')
        
        if c_code:
            data = Mentor.objects.filter(id=c_code.upper())
        else:
            data = None

        context = {
            'data': data
        }

        return render(request, 'search_mentor.html', context)
    