from django.shortcuts import render

# Create your views here.

def getIp(request):
    ip = request.session.get('ip',0)
    return render(request,'get_id_address_app/ip.html',{'ip':ip})
# get_id_address_app

def adarsh(request):
    return render(request,'get_id_address_app/adarsh.html')