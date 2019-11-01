from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import UserRegisterForm


def home(request):
	return render(request, 'job_board/home.html', {'title': 'HomePage'})
	
def about(request):
	return render(request, 'job_board/about.html', {'title': 'AboutPage'})
	
def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			messages.success(request, 'Account created!')
			return redirect('job_board-home')
	else:
		form = UserRegisterForm()
	return render(request,'users/register.html', {'form':form})






