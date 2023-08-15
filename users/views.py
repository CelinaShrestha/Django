from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def registerUsers(request):
    if request.method=="POST":
        username=request.POST.get("username")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")

        print(username,first_name,last_name,email,password,confirm_password)

        if password==confirm_password:
            users=User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password

            )
        users.save()
    return render(request,"index.html")

def loginUser(request):
    if(request.user.is_authenticated):
        return redirect("crud:home")
    else:
        if request.method=="POST":
            username=request.POST.get("username")
            password=request.POST.get("password")

            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("crud:home")
            else:
                print("User Validation Failed-401")
                return redirect("users:login")
    return render(request,"login.html")




def resetPass(request):
    if request.user.is_authenticated:
        return redirect("crud:home")
    else:
        if request.method=="POST":
            username=request.POST.get("username1")
            password=request.POST.get("password1")
            confirm_password=request.POST.get("confirm_password1")
            user=authenticate(request,username=username)
            user = User.objects.get(username=username)

            if user is not None and password == confirm_password:
                    user.set_password(password)
                    user.save()
                    return redirect("users:login")
            else:
                print("User Validation Failed-401")
                return redirect("users:reset")
    return render(request, "reset.html")


@login_required
def logoutUser(request):
    logout(request)
    return redirect("crud:home")
