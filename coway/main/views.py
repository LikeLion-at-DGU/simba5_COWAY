from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile, Post
from django.utils import timezone
# Create your views here.
def mainpage(request):
    return render(request, 'main/main.html')

def convpage(request):
    return render(request, 'main/conv/conv.html')

def cafeInfopage(request):
    return render(request, 'main/conv/cafe_info.html')

def cafeMappage(request):
    return render(request, 'main/conv/cafe_map.html')

def convInfopage(request):
    return render(request, 'main/conv/conv_info.html')

def convMappage(request):
    return render(request, 'main/conv/conv_map.html')

def restInfopage(request):
    return render(request, 'main/conv/rest_info.html')

def restMappage(request):
    return render(request, 'main/conv/rest_map.html')

def stdInfopage(request):
    return render(request, 'main/conv/std_info.html')

def stdMappage(request):
    return render(request, 'main/conv/std_map.html')

def joinpage(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            profile=Profile(user=user)
            profile.attendance += 1
            profile.save()
            auth.login(request, user)
            return redirect('mainpage')
    return render(request, 'main/login/join.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('mainpage')
        else:
            return render(request, 'main/login/login.html')
    elif request.method == 'GET':
        return render(request, 'main/login/login.html')

def logout(request):
    auth.logout(request)
    return redirect('mainpage')

def askpage(request):
    return render(request, 'main/myhome/ask.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.body = request.POST['body']
    new_post.author = request.user
    new_post.save()
    return redirect('homepage')

def editpage(request):
    return render(request, 'main/myhome/edit.html')

def homepage(request):
    return render(request, 'main/myhome/home.html')

def stpcafepage(request):
    return render(request, 'main/stamp/stamp_cafe.html')

def stpconvpage(request):
    return render(request, 'main/stamp/stamp_conv.html')

def stprestpage(request):
    return render(request, 'main/stamp/stamp_rest.html')

def stpstdpage(request):
    return render(request, 'main/stamp/stamp_std.html')

def easyroadpage(request):
    # if request.method == 'POST':
    #     sBuilding = request.POST.get('startBuilding')
    #     sFloor = request.POST.get('startFloor')
    return render(request, 'main/road/easy_road.html')

def roadchoicepage(request):
    return render(request, 'main/road/road_choice.html')

def shortroadpage(request):
    return render(request, 'main/road/short_road.html')