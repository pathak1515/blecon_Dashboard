from django.shortcuts import render
from django.shortcuts import redirect
from .models import hit
from function import hitsfunc
from .models import department
from .models import beacon
from .models import notification




def hits(request):
    hitsfunc()
    hits=1
    return render(request, 'adminlte/myhits.html', { 'hits':hit } )

def redirect_view(request):
    response = redirect('/admin/logout')
    return response
 
# def dept(request):
#     dept_data = department.objects.all()
#     return render(request, 'adminlte/department.html', {'dept_data':dept_data})

def dept(request):
   dept_data = department.objects.all()
   return render(request, 'adminlte/department.html', {'dept_data':dept_data} )

def bcn(request):
   beacon_data = beacon.objects.all()
   return render(request, 'adminlte/beacon.html', {'beacon_data':beacon_data} )

def notify(request):
    not_data = notification.objects.all()
    return render(request, 'adminlte/notification.html', {'not_data':not_data} )  
