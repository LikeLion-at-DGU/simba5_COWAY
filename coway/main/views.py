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
            nickname=request.POST['nickname']
            profile=Profile(user=user, nickname=nickname)
            profile.logintime = timezone.now()
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
            profile = Profile.objects.filter(user=user)
            if (timezone.now()-profile.logintime).days >= 1:
                profile.attendance += 1
            profile.logintime = timezone.now()
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

def listpage(request):
    post = Post.objects.filter(author=request.user)
    return render(request, 'main/myhome/list.html', {'posts' : post})

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.author = request.user
    new_post.save()
    return redirect('listpage')

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, 'main/myhome/detail.html', {'post':post})

def delete(request, id):
    delete_post = Post.objects.get(id=id)
    delete_post.delete()
    return redirect('listpage')

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
    return render(request, 'main/road/easy_road.html')

def roadchoicepage(request):
    return render(request, 'main/road/road_choice.html')

def shortroadpage(request):
    return render(request, 'main/road/short_road.html')