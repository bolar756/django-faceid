from django.shortcuts import render , redirect
from django.contrib.auth import logout, login , authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from django.http import HttpResponse ,JsonResponse
# Create your views here.

def Login (request):
       if request.method == "POST":
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user != None:
            message = messages.success(request,f'welcome {user.username}')
            auth.login(request,user)
            return redirect('/')
          else:
              message = messages.success(request,'user or wrong password')
              return render(request,'login.html')
       else:
            return render(request, 'login.html')
       
def signup(request):
     if request.method == "POST":
          username = request.POST['username']
          email = request.POST['email']
          password = request.POST['password']
          password1 = request.POST['password1']
          if User.objects.filter(email=email).exists():
              messages.error(request, 'Email address already exists.')
          if password == password1:
                  use = User.objects.create_user(email= email, username=username, password=password)
                  use.save()
                  user= authenticate(username=username, password=password)
                  if user:
                   login(request,user)
                   return redirect('setup')
                  else:
                       messages.info(request,'an error ocureed ')
          else:
               messages.info(request,'password should be the same ')
               return render(request, 'signup.html')
     else:
          return render(request,'signup.html')
     

def setup(request):
    if request.method == "POST":
            bio = request.POST['bio']
            photo = request.FILES.get('photo')  
            if photo:
              profile = Profile.objects.get(user=request.user)
              profile.bio = bio
              profile.photo = photo
              profile.save()  
              return redirect('home')
            else:
                 return HttpResponse('photo is none ')
    else:
        return render(request, 'setup.html')
