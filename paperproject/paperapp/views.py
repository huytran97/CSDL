from django.shortcuts import render
from . import forms
import sqlite3
import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    return render(request, 'home/home.html')

@login_required
def form_logout(request):
    logout(request)
    return render(request,'home/home.html', {'username' : False})


def form_login(request):
        if request.method == 'POST':
            username = request.POST.get('email')
            password =request.POST.get('password')
            user = authenticate(username=username, password=password)
            print(user)

            if user:
                login(request, user)
            
                return HttpResponseRedirect(reverse('index'))
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username,password))
                return HttpResponse("Invalid login details supplied.")
        else:
            return render(request, 'user/login.html')


def form_register(request):
    
    if request.method == 'POST':
        user_form = forms.Register(request.POST)
        if user_form.is_valid():
            conn = sqlite3.connect("db.sqlite3")
            cur = conn.cursor()
            # Find if user_form exists
            result = cur.execute('SELECT * FROM auth_user WHERE email=?',(user_form.cleaned_data['email'],))
            find_user = result.fetchone()
            print(find_user)
            if find_user:
                return HttpResponse('User is already existed')
            else:
                # Save User Form to Database
                user = user_form.save()

                # Hash the password
                user.set_password(user.password)

                # Update with Hashed password
                user.save()
                return HttpResponseRedirect(reverse('login'))
        else:
            return HttpResponse('Invalid input')
    else:
        user_form = forms.Register()
        return render(request, 'user/register.html',{'form' : user_form})


# Find all the papers in data.db
@login_required
def papers(request):
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS papers (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, time text, detail text, authors text)")
    result = cur.execute("SELECT * FROM papers")
    all_papers = result.fetchall()
    return render(request, 'paper_manage/papers.html', {'all_papers' : all_papers})


@login_required
def add_papers(request):
    if request.method == 'POST':
        # Get the data when user post the data
        paper_name = request.POST.get('paper_name')
        paper_no = request.POST.get('no')
        month = request.POST.get('month')
        year = request.POST.get('year')
        time = 'Tháng {} năm {}'.format(month,year)
        authors = request.POST.get('authors')
        conn = sqlite3.connect("db.sqlite3")

        # Insert to data.db
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS papers (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, time text, detail text, authors text)")
        query = "INSERT INTO papers VALUES (null,?,?,?,?)"
        cur.execute(query, (paper_name,paper_no,time,authors))
        result = cur.execute("SELECT * FROM papers")
        all_papers = result.fetchall()
        conn.commit()
        conn.close()   
        if all_papers:
            return render(request, 'paper_manage/papers.html', {'all_papers' : all_papers})
    return render(request, 'paper_manage/add_papers.html')