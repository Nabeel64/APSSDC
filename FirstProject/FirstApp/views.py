from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from FirstApp.models import Register
# Create your views here.
def home(request):
    return HttpResponse("Hello World")
def ht(request):
    return HttpResponse("<h2>Hello World</h2>")
def usernameprint(request,uname):
    return HttpResponse("<h3>Hello World <span style='color:green'>{}</span></h3>".format(uname))
def us(request,uname,age):
    return HttpResponse("<h3>Hi {} and your age is {}</h3>".format(uname,age))
def empdetails(request,eid,ename,eage):
    return HttpResponse("<h3><script>alert('hi welcome {}')</script>hi Welcome {} your age is {} and your empid is {}</h3>".format(ename,ename,eage,eid))
def htm(request):
    return render(request,'html/sample.html')
def html(request, uname):
    return render(request,'html/sample1.html',{'n':uname})
def details(request,uname,id):
    y={'n':uname,'i':id}
    return render(request,'html/sample2.html',y)

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internalJS(request):
	return render(request,'html/internalJS.html')
def myform(request):
    if request.method == "POST":
        #print(request.POST)

        uname = request.POST['uname'] # prints individual data
        rollno = request.POST['rollno'] # prints individual data
        email = request.POST['email'] # prints individual data and also can use POST.get('VarName')
        #print(uname,rollno,email)

        data = {'username':uname,'rno':rollno,'email':email}
        return render(request,'html/display.html',data)
    return render(request,'html/myform.html')

def reg(req):
    if req.method=="POST":
        fn = req.POST['fn']
        ln=req.POST['ln']
        email=req.POST['email']
        phone=req.POST['phone']
        gender=req.POST['gender']
        address=req.POST['address']
        language=req.POST.getlist('language')
        hob=req.POST['hob']
        regdata = {'firstname':fn,'lastname':ln,'email':email,'number':phone,'gender':gender,'address':address,'language':language,'hobbies':hob}
        return render(req,'html/output.html',regdata)
    return render(req,'html/register.html')

def log(req):
    if req.method=="POST":
        uname=req.POST['uname']
        pwd=req.POST['pwd']
        if(uname=="Manish" and pwd=="1234"):
            return HttpResponse("<h3><script>alert('Valid')</script></h3>")
        else:
            return HttpResponse("<h3><script>alert('Invalid')</script></h3>")
    
    return render(req,'html/login.html')

def bootstrapfun(request):
    return render(request,'html/sampleboot.html')

def btregi(request):
    return render(request,'html/btregst.html')
def reg(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        r=Register(name=name,email=email)
        r.save()
        return HttpResponse("Row insertion successfully")
    return render(request,'html/reg.html')

def display(request):
    data=Register.objects.all()
    return render(request,'html/display1.html',{'data':data})
def sview(request,y):
    w = Register.objects.get(id=y)
    return render(request,'html/sview.html',{'y':w})
    #return HttpResponse("Your Name is : {} and your email id is: {}".format(w.name,w.email))
def supt(request,q):
    t = Register.objects.get(id=q)
    if request.method == "POST":
        na = request.POST['n']
        em = request.POST['e']
        t.name = na
        t.email = em
        t.save()
        return redirect('/display')
    return render(request,'html/supdate.html',{'p':t})
def sndl(request,p):
    b = Register.objects.get(id=p)
    if request.method == "POST":
        b.delete()
        return redirect('/display/')
    return render(request,'html/sndlt.html',{'z':b})