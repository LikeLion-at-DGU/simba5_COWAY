from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request, 'main/main.html')

def convpage(request):
    return render(request, 'main/conv/conv.html')

def convinfopage(request):
    return render(request, 'main/conv/conv_info.html')

def convmappage(request):
    return render(request, 'main/conv/conv_map.html')

def joinpage(request):
    return render(request, 'main/login/join.html')

def loginpage(request):
    return render(request, 'main/login/login.html')

def askpage(request):
    return render(request, 'main/myhome/ask.html')

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