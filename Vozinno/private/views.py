from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from private.forms import CreateEmailForm, CreateDetailsForm, RegisterationForm
from private.models import Email,Details
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginpage')
def createemail(request):
    form=CreateEmailForm
    context={}
    context['form']=form
    qs=Email.objects.all()
    context['qs']=qs
    if request.method=="POST":
        form=CreateEmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("createemail")
    return render(request,"private/createemail.html",context)

@login_required(login_url='loginpage')
def editmail(request,pk):
    form=Email.objects.get(id=pk)
    form=CreateEmailForm(instance=form)
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = Email.objects.get(id=pk)
        form = CreateEmailForm(instance=form, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createemail")
    return render(request,"private/editmail.html",context)

@login_required(login_url='loginpage')
def deletemail(request, pk):
    entry = Email.objects.get(id=pk)
    entry.delete()
    form = CreateEmailForm
    context = {}
    context['form'] = form
    qs = Email.objects.all()
    context['qs'] = qs
    return redirect("createemail")

@login_required(login_url='loginpage')
def createdetails(request):
    form = CreateDetailsForm
    context = {}
    context['form'] = form
    details = Details.objects.all()
    context['details'] = details
    if request.method == "POST":
        form = CreateDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("createdetails")
    return render(request, "private/createdetails.html", context)

@login_required(login_url='loginpage')
def detailsview(request, pk):
    obj = Details.objects.get(id=pk)
    context = {}
    context['details'] = obj
    return render(request, "private/detailsview.html", context)

@login_required(login_url='loginpage')
def detailsedit(request, pk):
    form = Details.objects.get(id=pk)
    form = CreateDetailsForm(instance=form)
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = Details.objects.get(id=pk)
        form = CreateDetailsForm(instance=form, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("createdetails")
    return render(request, "private/editdetails.html", context)

@login_required(login_url='loginpage')
def detailsdelete(request, pk):
    entry = Details.objects.get(id=pk)
    entry.delete()
    form = CreateDetailsForm
    context = {}
    context['form'] = form
    qs = Details.objects.all()
    context['qs'] = qs
    return redirect("createdetails")


def Register(request):
    form = RegisterationForm()
    context = {'form': form}
    if request.method == "POST":
        form = RegisterationForm(request.POST)
        print("im here")
        if form.is_valid():
            form.save()
            return redirect('loginpage')
        else:
            context = {}
            context['form'] = form
            return render(request, 'private/registeration.html', context)
        return render(request, 'private/registeration.html', context)

    return render(request, 'private/registeration.html', context)

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pwd")
        print(username, ',', password)
        if ((username == "admin") & (password == "admin")):
            return render(request, "private/index.html")
        else:
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('loginpage')
    return render(request, 'private/loginpage.html')


def index(request):
    details = Details.objects.all()
    context = {}
    context['details'] = details
    return render(request, 'private/index.html', context)

@login_required(login_url='loginpage')
def logOut(request):
    logout(request)
    return redirect("loginpage")