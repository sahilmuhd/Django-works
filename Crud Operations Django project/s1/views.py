from django.shortcuts import render

# Create your views here.
def loadpage1(request):
    return render(request,'page1.html')
def sub1(request):
    name=request.POST['txtName']
    request.session['customername']=name
    return render(request,'page2.html')
def sub2(request):
    email=request.POST['txtEmail']
    request.session['customeremail']=email
    return render(request,'page3.html')
def sub3(request):
    mobile=request.POST['txtMobile']
    print(request.session.get('customername', ''))
    print(request.session.get('customeremail', ''))
    return render(request,'page4.html')
def sub4(request):
    name=request.POST['txtName']
    return render(request,'page5.html')
