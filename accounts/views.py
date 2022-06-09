from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.views import View
from django.views.generic import ListView,DetailView
# Create your views here.

class RegisterView(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        email = request.POST["email"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request, 'Email taken')
                return redirect('register')
            else:

                user = User.objects.create_user(username=username, email=email, password=password1, first_name=first_name,
                                        last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')

        else:
            messages.warning(request, 'Password not matching')
            return redirect('register')

        return redirect('/')



class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(password=password, username=username)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.warning(request, 'invalid credentials')
            return redirect('login')



class LogoutView(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')




