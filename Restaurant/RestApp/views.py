from django.shortcuts import render,redirect
from django.http import HttpResponse
from RestApp.forms import ReForm,ItemsForm,UsgForm,Rltype,Rlupd,pfupd,chgepwd
from RestApp.models import Restaurant,Itemlist,Rolereq,User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from Restaurant import settings
# Create your views here.
def home(request):
	w=Restaurant.objects.filter(uid_id=request.user.id)
	t=Restaurant.objects.all()
	return render(request,'app/home.html',{'c':w,'y':t})
def about(request):
	return render(request,'app/about.html')
def contact(request):
	return render(request,'app/contact.html')

@login_required
def restlist(request):
	y=Restaurant.objects.filter(uid_id=request.user.id)
	if request.method=="POST":
		t=ReForm(request.POST,request.FILES)
		if t.is_valid():
			c=t.save(commit=False)
			c.uid_id=request.user.id 
			c.save()
			messages.success(request,"Restaurant added succesfully!")
			return redirect('/rlist')
	t=ReForm()
	return render(request,'app/restaurantlist.html',{'q':t,'a':y})

@login_required

def rstup(request,m):
	k=Restaurant.objects.get(id=m)
	if request.method=="POST":
		e=ReForm(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.success(request,"{} Restaurant updates succesfully!".format(k.rname))
			return redirect('/rlist')
	e=ReForm(instance=k)
	return render(request,'app/restupdate.html',{'x':e})
@login_required
def rstdl(request,n):
	v = Restaurant.objects.get(id=n)
	if request.method == "POST":
		messages.info(request,"{} Restaurant deleted succesfully!".format(v.rname))
		v.delete()
		return redirect('/rlist')
	return render(request,'app/restdelete.html',{'q':v})
@login_required

def rstvw(request,a):
	s=Restaurant.objects.get(id=a)
	return render(request,'app/restview.html',{'z':s})
@login_required

def itlist(request):
	st=list(Restaurant.objects.filter(uid_id=request.user.id))
	mm = Itemlist.objects.all()
	d,i={},0
	for mp in mm:
		for h in st:
			if h.id == mp.rsid_id:
				d[i]=mp.iname,mp.icategory,mp.price,mp.iimage,mp.itavailability,mp.id,h.rname
				i=i+1
		print(d)

	if request.method == "POST":
		k = ItemsForm(request.POST,request.FILES)
		if k.is_valid():
			k.save()
			messages.success(request,'Item is Added successfully')
			return redirect('/ilist/')
	k=ItemsForm()
	return render(request,'app/itmlist.html',{'r':k,'er':st,'s':d.values()})

def usrreg(request):
	if request.method=="POST":
		d=UsgForm(request.POST)
		if d.is_valid():
			d.save()
			return redirect('/rg')
	d=UsgForm()
	return render(request,'app/usrregister.html',{'t':d})

def Itup(request,m):
	k=Itemlist.objects.get(id=m)
	if request.method=="POST":
		e=ItemsForm(request.POST,request.FILES,instance=k)
		if e.is_valid():
			e.save()
			messages.success(request,"{} item updated succesfully!".format(k.iname))
			return redirect('/ilist')
	e=ItemsForm(instance=k)
	return render(request,'app/Itupdate.html',{'x':e})

def Itdl(request,n):
	v = Itemlist.objects.get(id=n)
	if request.method == "POST":
		messages.info(request,"{} item deleted succesfully!".format(v.iname))
		v.delete()
		return redirect('/ilist')
	return render(request,'app/Itdelete.html',{'q':v})
@login_required
def rolereq(request):
	if request.method == "POST":
		k = Rltype(request.POST,request.FILES)
		if k.is_valid():
			print(k)
			y = k.save(commit=False)
			y.ud_id = request.user.id
			y.uname = request.user.username
			y.save()
			return redirect('/')
	k = Rltype()
	return render(request,'app/rolereq.html',{'d':k})

@login_required
def gveperm(request):
	u=User.objects.all()
	r=Rolereq.objects.all()
	d={}
	for n in u:
		for m in r:
			if n.is_superuser == 1 or n.id!=m.ud_id:
				continue
			else:
				d[m.id]=m.uname,m.rltype,n.role,n.id,m.id
	return render(request,'app/gvpl.html',{'h':d.values()})

@login_required
def gvupd(request,t):
	y=Rolereq.objects.get(ud_id=t)
	d=User.objects.get(id=t)
	if request.method=="POST":
		n=Rlupd(request.POST,instance=d)
		if n.is_valid():
			n.save()
			y.is_checked=1
			y.save()
			return redirect('/gvper')
	n=Rlupd(instance=d)
	return render(request,'app/gvepermission.html',{'c':n})
@login_required
def pfle(request):
	return render(request,'app/profile.html')

@login_required
def feedback(request):
	if request.method=="POST":
		sd=request.POST['snmail']
		sm=request.POST['sub']
		mg=request.POST['msg']
		rt=settings.EMAIL_HOST_USER
		dt=send_mail(sm,mg,rt,[sd])
		if dt==1:
			return redirect('/')
	return render(request,'app/feedback.html')
@login_required
def rdlt(request,n):
	y=Rolereq.objects.get(id=n)
	k=User.objects.get(id=y.ud_id)
	if request.method=="POST":
		k.role=1
		k.save()
		y.delete()
		return redirect('/gvper')

	return render(request,'app/reqdelete.html',{'q':k})
@login_required
def pfleupd(request):
	t=User.objects.get(id=request.user.id)
	if request.method=="POST":
		pfl=pfupd(request.POST,request.FILES,instance=t)
		if pfl.is_valid():
			pfl.save()
			return redirect('/pfle')

	pfle=pfupd(instance=t)
	return render(request,'app/pfleupdate.html',{'u':pfle})
@login_required
def changepwd(request):
	if request.method=="POST":
		k=chgepwd(user=request.user,data=request.POST)
		if k.is_valid():
			k.save()
			return redirect('/login')
	k = chgepwd(user=request)
	return render(request,'app/changepwd.html',{'t':k})