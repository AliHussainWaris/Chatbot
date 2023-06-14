from django.http import HttpResponse
from django.shortcuts import render, redirect
from aiml import Kernel
from Project.run import aimlfun
from Project.Queries.signup import signup
from Project.Queries.login import login
from Project.Queries.data import datasend
from Project.Queries.fetch import chatfetch

aiml_kernel = Kernel()
name = ''

def Home(request):
    name = request.COOKIES.get('name')
    if name:
        if request.method == 'POST':
            user = request.POST.get('message', '')
            bot_response = aimlfun(user , name)
            datasend(name , user , bot_response)
            chat = chatfetch(name)
            
            userChat = "|".join(chat[1])
            botChat = "|".join(chat[0])
            
            return render(request, "View/index.html", {'user': user, 'bot_response': bot_response, 'name': name, 'userchat': userChat, 'botchat': botChat})
        
    else:
        return redirect('/Login')
    
    return render(request, "View/index.html", {'name': name})


def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        name = login(email, password)
        if name:
            response = redirect("/")
            response.set_cookie('name', name)  # Set the cookie with the name
            return response
        else:
            return render(request, "View/Login/Login.html", {'error_message': 'Invalid credentials'})

    return render(request, "View/Login/Login.html")

def Signup(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        signup(name, email, password)
        return redirect("/Login")

    return render(request, "View/Signup/Signup.html")
