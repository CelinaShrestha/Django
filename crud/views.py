from django.shortcuts import render,redirect
from .models import Blog,Contact #manager->objects
from django.core.paginator import Paginator
from myproject.settings import EMAIL_HOST_USER #replace root with your project name
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required


from .forms import BlogForm

# Create your views here.
def homepage(request):
    blog=Blog.objects.all()
    paginator = Paginator(blog, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data = request.GET.get("search")
    context = {
        "blogs":page_obj,
        "page_obj":page_obj
    }
    if(data is not "" and data is not None ):
        searchData=Blog.objects.filter(title__contains=data)
        print(searchData)
        return render(request,"crud/index.html",{"blog":searchData})
         

    return render(request,"crud/index.html",context)

def particularData(request,id):
    blog=Blog.objects.get(id=id)
    context ={"blog":blog}
    return render(request,"crud/post.html",context)

@login_required
def create(request):
    forms = BlogForm(request.POST or None)

    if(forms.is_valid()):
        forms.save()
        return redirect("crud:home")

    return render(request,"crud/creates.html",{"forms":forms})



def contacts(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        subject = "Wants to Collaborate!!!"
        recipient = "someone@yopmail.com","hplaptop7821@gmail.com",
       
        cont =Contact.create(name,message,email)
        cont.save()
        template = render_to_string('crud/email.html',{'name':name,'description':message,'mail':email})
        email=EmailMessage(subject,template,EMAIL_HOST_USER,recipient)


        email.fail_silently=False
        if email!=None:
            email.send()

        
    return render(request,"crud/contact.html")

def deleteData(request,id):
    blog=Blog.objects.get(id=id)
    blog.delete()
    return redirect("crud:home")

def updateData(request,id):
    blog=Blog.objects.get(id=id)
    forms=BlogForm(request.POST or None,instance=blog)
    context = {
        "forms":forms,
        "title":blog.title,
        "subtitle":blog.subtitle,
        "description":blog.description
    }
    if forms.is_valid():
        forms.save()
        return redirect("crud:home")

    return render(request,"crud/creates.html",context)
   