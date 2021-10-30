
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages


# Create your views here.
def registerPage(request):
	form = CreateUserForm()

	if request.method == 'POST':
		print("hello")
		form = CreateUserForm(request.POST)
		
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			role = form.cleaned_data.get('first_name')
			print("username=",username,"password=",password,"role=",role)
			
			

			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form':form}



	return render(request, 'register.html', context)
def login_request(request):
	if request.method == 'POST':
		
		username = request.POST.get('username')
		password =request.POST.get('password1')
		role = request.POST.get('first_name')
	

		
		
		

		user = authenticate(request, username=username, password=password)



		

		if user is not None:
			if(user.first_name=="admin"):
				
				return redirect('accept')
			elif(user.first_name=="cc"):
				return redirect('ccpage')
			elif(user.first_name=="student" and role=="student"):
				return redirect('student')

		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)
def logoutUser(request):
	logout(request)

	return render(request,'login.html')
def accept(request):
	return render(request,"admpage.html")
def ccpage(request):
	return render(request,"ccpage.html")
def add_event(request):
	if request.method == 'POST':
		
		name= request.POST.get('name')
		club_name =request.POST.get('club_name')
		description = request.POST.get('description')
		loc= request.POST.get('loc')
		date= request.POST.get('date')
		user=events.objects.create(name=name ,club_name=club_name,loc=loc,date=date)
		user.save() 
		print("yo yo!!")
		return redirect('ccpage')


	return render(request,"addevent.html")
def club(request):
	if request.method == 'GET':
		x=clubs.objects.all()
		context = {'x':x}
		return render(request, 'viewclub.html', context)
def view_events(request,pk):
	
	x = events.objects.filter(club_name=pk)

	context = {'x':x}
	return render(request, 'view_events.html', context)
def student_club(request):
	
	if request.method == 'GET':
		x=clubs.objects.all()
		context = {'x':x}
		return render(request, 'stu_club.html', context)
def stu_view_events(request,pk):
	x = events.objects.filter(club_name=pk)

	context = {'x':x}
	return render(request, 'stu_events.html', context)

def student(request):
	return render(request, 'student.html')
def registration_form(request):
	if request.method == 'POST':
		
		name= request.POST.get('name')
		roll_no =request.POST.get('roll_no')
		email = request.POST.get('email')
		phone= request.POST.get('phone')
		event= request.POST.get('event')
		club= request.POST.get('club')
		user=registration.objects.create(name=name ,roll_no=roll_no,email=email,phone=phone,event=event)
		user.save() 
		
		return redirect('student')
	return render(request,'registration_form.html')
def reg_part(request,pk):
	x = registration.objects.filter(event=pk)

	context = {'x':x}
	return render(request, 'participants.html', context)
def faq(request):
	return render(request,'faq.html')


