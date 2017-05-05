from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#  views for students
def students_list(request):
    return render(request, 'students/students_list.html', {})

def students_add(request):
    return HttpResponse('0students_add, %s')

def students_delete(request,sid):
    return HttpResponse('students_delete %s' % sid)

def students_edit(request,sid):
    return HttpResponse('students_edit%s' % sid)


#  views for groups
def groups_list(request):
    return HttpResponse('Groups')

def groups_add(request):
    return HttpResponse('groups_add')

def groups_delete(request, gid):
    return HttpResponse('groups_add%s' % gid)

def groups_edit(request, gid):
    return HttpResponse('groups_add%s' % gid)

