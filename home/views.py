from django.shortcuts import render, HttpResponse, redirect

# for automatic created form
from django.contrib.auth.forms import UserCreationForm

# importing forms and user from models
from django import forms
from django.contrib.auth.models import User

# for user form
from .models import *
from .forms import CreateUserForm

# for message
from django.contrib import messages

# for authentication
from django.contrib.auth import authenticate, login, logout

# for required login
from django.contrib.auth.decorators import login_required

# register

import requests
def registerPage(request):

    # if registered in then no  register page can open
    if request.user.is_authenticated:
        return redirect('home')

    else:
        form= CreateUserForm()
        if request.method == 'POST':

            #user created form
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                # save name of user for flash message
                user= form.cleaned_data.get('username')

                # flash message
                messages.success(request, 'Account was created for ' + user)

                # to redirect to login page
                return redirect('login')

        context={'form':form}
        return render(request,'register.html',context)


#login

def loginPage(request):

    # if logged in then no login or register page can open
    if request.user.is_authenticated:
        return redirect('home')

    # otherwise login page will open
    else:
        if request.method == 'POST':

            # TO GET USERNAME AND PASSWORD
            username = request.POST.get('username')
            password = request.POST.get('password')

            # authenticate
            user= authenticate(request, username=username, password=password)

            # if user is present then redirect to homepage 
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Username or password is incorrect')

        context={}
        return render(request,'login.html',context)

# logout

def logoutUser(request):
    logout(request)
    return redirect('home')

# summarisation

# login required
@login_required(login_url='login')

def index(request):
    if request.method == "POST":
        text = request.POST.get('text')
        API_URL = " enter_api"
        headers = {"Authorization": "enter key"}

        
        maxL = int(request.POST.get('maxL'))
        minL=maxL//4
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        output = query({
            "inputs": text,
            "parameters":{"min_length":minL,"max_length":maxL},
        })[0]
        context={
            'variable':output["summary_text"],
        }
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')   


# homepage   

def index2(request):
    return render(request,'Homepage.html')


# question answers

# login required
@login_required(login_url='login')

def questions(request):
    if request.method == "POST":
        text = request.POST.get('text')
        question= request.POST.get('question')
        # print(text)
        # print(question)
        API_URL = "enter_api"
        headers = {"Authorization": "enter_key"}

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
            
        output = query({
            "inputs": {
                "question": question,
                "context": text,
            },
        })
        print(output)
        context={
            'variable':output['answer'],
        }
        return render(request,'questions.html',context)
    else:
        return render(request,'questions.html')
    

def about(request):
    return HttpResponse("this is about page")

def error_404(request, exception):
    return render(request, '404.html')


