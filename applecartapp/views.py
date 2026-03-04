from django.shortcuts import render
from .models import Buy
# Create your views here.
def index(request):
    return render (request, 'index.html')

def buy(request):
    if request. method == "POST":
        name=request.POST.get("name")
        mobile=request.POST.get("mobile")
        pincode=request.POST.get("pincode")
        address=request.POST.get("address")
        buy=Buy(name=name,mobile= mobile, pincode=pincode, address=address)
        buy.save()
    return render (request, 'buy.html')