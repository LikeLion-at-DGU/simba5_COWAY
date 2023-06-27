from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile, Post, Info, Bookmark
from haversine import haversine
import heapq
from django.utils import timezone
from django.http import HttpResponse

# Create your views here.
arr = [[-1 for j in range(246)] for i in range(246)]
infos = Info.objects.all()
cnt = 1
for i in infos:
    num = i.near.split(" ")
    for j in num:
        spot = (i.latitude, i.longitude)
        num2 = Info.objects.get(id=j)
        spot2 = (num2.latitude, num2.longitude)
        if spot == spot2:
            arr[cnt][int(j)] = 0
        else:
            arr[cnt][int(j)] = haversine(spot, spot2) * 1000
    cnt += 1
for i in range(cnt):
    for j in range(cnt):
        if arr[i][j] == -1:
            arr[i][j] = float('inf')
visit = [0] * cnt
dist = [float('inf')] * cnt
prev = [0] * cnt
def find():
    min = float('inf')
    v = 0
    for i in range(cnt):
        if visit[i] == 0 and min > dist[i]:
            min = dist[i]
            v = i
    return v
def check():
    for i in range(cnt):
        if visit[i] == 0:
            return 1
    return 0
def Dijkstra(start, end):
    dist[start] = 0
    heap = [(0, start)]  # 우선순위 큐 (거리, 노드)로 구성
    while heap:
        d, v = heapq.heappop(heap)
        if v == end:
            break
        if d > dist[v]:
            continue
        for i in range(cnt):
            if dist[i] > dist[v] + arr[v][i]:
                dist[i] = dist[v] + arr[v][i]
                prev[i] = v
                heapq.heappush(heap, (dist[i], i))
                if i == end:  # 도착점에 도달한 경우, 최단 경로를 찾았으므로 탐색 종료
                    return dist[i]

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
            name=request.POST['name']
            profile=Profile(user=user, name=name)
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
    pro = Profile.objects.get(user=request.user)
    new_post.email = pro.name
    new_post.save()
    return redirect('homepage')

def editpage(request):
    if request.method == 'POST':
        origin = request.POST['originpassword']
        password = request.POST['password']
        confirm = request.POST['confirm']
        if origin is not password and password == confirm:
            user = request.user
            user.set_password(password)
            user.save()
            auth.logout(request)
            return redirect('loginpage')
    return render(request, 'main/myhome/edit.html')

def homepage(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'main/myhome/home.html', {'profile': profile})

def bookmarkpage(request):
    if request.method == 'POST':
        new_bookmark = Bookmark()
        new_bookmark.user = request.user
        new_bookmark.startbuilding = request.POST['startBuilding']
        new_bookmark.startfloor = request.POST['startFloor']
        new_bookmark.endbuilding = request.POST['endBuilding']
        new_bookmark.endfloor = request.POST['endFloor']
        new_bookmark.save()
    bookmark = Bookmark.objects.filter(user=request.user)
    count = 0
    for book in bookmark:
        count += 1
    return render(request, 'main/bookmark/bookmark.html', {'bookmarks':bookmark, 'count':count})

def deletebookmark(request, id):
    delete_bookmark = Bookmark.objects.get(id=id)
    delete_bookmark.delete()
    return redirect('bookmarkpage')

def easyroadpage(request):
    if request.method == 'POST':
        start_building = request.POST.get('startBuilding')
        start_floor = request.POST.get('startFloor')
        end_building = request.POST.get('endBuilding')
        end_floor = request.POST.get('endFloor')

        context = {
            'start_building': start_building,
            'start_floor': start_floor,
            'end_building': end_building,
            'end_floor': end_floor,
        }

        return render(request, 'main/road/easy_road.html', context)
    elif request.method == 'GET':
        start_building = request.GET.get('startBuilding')
        start_floor = request.GET.get('startFloor')
        end_building = request.GET.get('endBuilding')
        end_floor = request.GET.get('endFloor')

        context = {
            'start_building': start_building,
            'start_floor': start_floor,
            'end_building': end_building,
            'end_floor': end_floor,
        }

        return render(request, 'main/road/easy_road.html', context)
    else:
        return redirect('roadchoicepage')

def roadchoicepage(request):
    return render(request, 'main/road/road_choice.html')

def shortroadpage(request):
    if request.method == 'POST':
        for i in range(cnt):
            dist[i] = float('inf')
            visit[i] = 0
            prev[i] = 0
        start_building = request.POST.get('startBuilding')
        start_floor = request.POST.get('startFloor')
        end_building = request.POST.get('endBuilding')
        end_floor = request.POST.get('endFloor')
        start_in = Info.objects.filter(name=start_building)
        end_in = Info.objects.filter(name=end_building)
        start_info = start_in.get(floor=start_floor)
        end_info = end_in.get(floor=end_floor)
        distance = round(Dijkstra(start_info.id, end_info.id))
        time = round(distance / 65)
        path = []
        curr = end_info.id
        while curr != 0:
            path.append(curr)
            curr = prev[curr]
        infos = [get_object_or_404(Info,id=a) for a in path[::-1]]
        context = {
            "infos": infos,
            'start_building': start_building,
            'start_floor': start_floor,
            'end_building': end_building,
            'end_floor': end_floor,
            'distance': distance,
            'time': time,
        }

        return render(request, 'main/road/short_road.html', context)
    elif request.method == 'GET':
        for i in range(cnt):
            dist[i] = float('inf')
            visit[i] = 0
            prev[i] = 0
        start_building = request.GET.get('startBuilding')
        start_floor = request.GET.get('startFloor')
        end_building = request.GET.get('endBuilding')
        end_floor = request.GET.get('endFloor')
        start_in = Info.objects.filter(name=start_building)
        end_in = Info.objects.filter(name=end_building)
        start_info = start_in.get(floor=start_floor)
        end_info = end_in.get(floor=end_floor)
        distance = round(Dijkstra(start_info.id, end_info.id))
        time = round(distance / 65)
        path = []
        curr = end_info.id
        while curr != 0:
            path.append(curr)
            curr = prev[curr]
        infos = [get_object_or_404(Info,id=a) for a in path[::-1]]
        context = {
            "infos": infos,
            'start_building': start_building,
            'start_floor': start_floor,
            'end_building': end_building,
            'end_floor': end_floor,
            'distance': distance,
            'time': time,
        }
        return render(request, 'main/road/short_road.html', context)
    else:
        return redirect('roadchoicepage')