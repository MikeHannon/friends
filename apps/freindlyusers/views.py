from django.shortcuts import render,redirect

# Create your views here.
from .models import User, Friendship

def index(request):
    users = User.objects.all()
    return render(request, 'freindlyusers/index.html', {'users':users})

def addUser(request):
    if request.method == "POST":
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    return redirect('/')

def addFriend(request):
    if request.method == "POST":
        f1 = User.objects.filter(pk=request.POST['f1'])
        f2 = User.objects.filter(pk=request.POST['f2'])
        if f1 and f2:
            Friendship.objects.create(user1=f1[0], user2=f2[0])
    return redirect('/')

def showUser(request,id):
    if request.method == "GET":
        try:
            user = User.objects.get(pk=id)
            print user
            print user.f2
        except:
            return redirect('/')
    else:
        return redirect('/')
    return render(request,"freindlyusers/show.html", {"user":user})
