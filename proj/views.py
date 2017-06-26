from django.http import HttpResponse
from django.shortcuts  import render
from database import models

def home_view(request):
	value=request.META['HTTP_REFERER']
	return HttpResponse(value);
	#return  render(request,request.META['REMOTE_ADDR']);


def search_view(request):
	if (request.GET) :
		key=request.GET['q']
		emp_obj=models.Employee.objects.filter(Name__icontains=key)
		return render(request, "search_result.html", {'employees':emp_obj,'query':key })
	else:
		return render(request, 'search_form.html');


def search_res(request):
	key=request.GET['q']
	return HttpResponse(key);



def emp_detail_view(request):
		emp_id=request.GET['emp_id']
		try:
			emp=models.Employee.objects.get(Emp_Id=emp_id)
		except:
			emp=None
		return render(request, "emp_details.html", {'employee':emp })

