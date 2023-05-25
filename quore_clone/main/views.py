from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Question,Answer
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.admin import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
user=None
user_name=""
def home(req):
    return render(req, 'main/login.html')

def main(req):
    global login,user_id
    questions=Question.objects.all()
    answer=Answer.objects.all()
    users=User.objects.all()
    if req.method == "POST":
        category = req.POST.get("category").lower()
        user_query = req.POST.get("input").lower()
        if category == "person":
            questions=User.objects.filter(username__icontains=user_query)
        elif category == "question":
            questions = Question.objects.filter(title__icontains=user_query)
    content={
        "questions":questions,
        "answers":answer,
        "users":users,
        "user":user,
    }
    return render(req,"main/main.html",content)

def sign_in(req):
    if req.method == "POST":
        username=req.POST.get("name")
        email=req.POST.get("mail")
        password=req.POST.get("password")
        myuser=User.objects.create_user(username,email,password)
        myuser.is_superuser = True
        myuser.is_staff = True
        myuser.save()
    return render(req, 'main/sign_in.html')

def log_in(req):
    global user,user_name
    username=req.POST.get("username")
    password=req.POST.get("password")
    user=authenticate(username=username,password=password)
    if user is not None:
        user_name=username
        l=login(req,user)
        return HttpResponseRedirect(reverse("home"))
    return render(req,"main/login.html")

def log_out(req):
    logout(req)
    return HttpResponseRedirect(reverse("log_in"))

def email_check(req):
    ind=0
    data=User.objects.all()
    email_data=[ con.email for con in data]
    username=[con.username for con in data]
    user_mail=req.POST.get("mail")
    user_name=req.POST.get("username")
    if user_mail:
        if user_mail in email_data:
            ind=1
    if user_name:
        if user_name in username:
            ind=1
    return HttpResponse(ind)


def problem_post(req):
    global user_name
    print(user_name)
    if req.method == "POST":
        title=req.POST.get("title")
        desc=req.POST.get("description","")
        print(user_name)
        if req.user.is_authenticated:
            user = req.user
        if title :
            obj=Question(title=title,description=desc,user=user)
            obj.save()
    return render(req,"main/postprob.html")

def view(req,slug):
    question=Question.objects.get(slug=slug)
    ans=Answer.objects.filter(question=question.id)
    content={
        "question":question,
        "ans" : ans
    }
    if req.user.is_authenticated:
            user = req.user
    if req.method == "POST":
        user_content=req.POST.get("description","") 
        if user_content:
            user_ans=Answer(content=user_content,question=question,user=user)
            user_ans.save()
    return render(req,"main/views.html",content)