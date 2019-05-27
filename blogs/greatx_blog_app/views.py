from django.shortcuts import render
from .models import Registration,BlogDetails
from .serializers import RegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator


def registrationForm(request):
    return render(request,'registrationform.html')

def saveUserDetails(request):
    firstname = request.POST.get('firstname')
    lastname = request.POST.get('lastname')
    contactno = request.POST.get('contactno')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user_id = request.POST.get('user_id')
    Registration(firstname=firstname,lastname=lastname,contactno=contactno,username=username,email=email,password=password,user_id=user_id).save()  
    messages.error(request,'Successfully Registered')
    return HttpResponseRedirect("/")

def enterBlogDetails(request):
    data = Registration.objects.all()
    return render(request,'blogdetails.html',{'object_list':data})

def saveBlogDetails(request):
    if request.method == 'POST' and request.FILES['image']:
        author = request.POST.get('author')
        author = Registration.objects.get(username=author)
        title = request.POST.get('title')
        shortdescription = request.POST.get('shortdescription')
        longdescription = request.POST.get('longdescription')
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        published_date = request.POST.get('published_date')
        BlogDetails(author=author,title=title,shortdescription=shortdescription,longdescription=longdescription,image=uploaded_file_url,published_date=published_date).save()
        messages.error(request,'Blog Added')
        return HttpResponseRedirect("/")

def viewBlogDetails(request):
    blog_list = BlogDetails.objects.all()
    paginator = Paginator(blog_list,10)    
    page = request.GET.get('page')   
    blog = paginator.get_page(page)    
    return render(request,'viewallblogdetails.html',{'object_list':blog})

def editBlog(request):
    blog_id = request.GET.get('edit')
    data = Registration.objects.all()
    data1 = BlogDetails.objects.filter(id=blog_id)
    return render(request,'blogdetails.html',{'blog_id':blog_id,'object_data':data1,'object_list':data})

def editBlogDetails(request):
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        author = request.POST.get('author')
        author = Registration.objects.get(username=author)
        title = request.POST.get('title')
        shortdescription = request.POST.get('shortdescription')
        longdescription = request.POST.get('longdescription')    
        published_date = request.POST.get('published_date')    
        uploaded_file_url = None
        if request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name,image)
            uploaded_file_url = fs.url(filename)
        blog = BlogDetails.objects.filter(id=blog_id).first()
        if blog:
            blog.author = author
            blog.title = title
            blog.shortdescription = shortdescription
            blog.longdescription = longdescription
            if uploaded_file_url:
                blog.image = uploaded_file_url
            blog.save()
        messages.error(request,'Blog Updated')
        return HttpResponseRedirect("/")    

def deleteBlogDetails(request):
    blog_id = request.GET.get('del')    
    BlogDetails.objects.filter(id=blog_id).delete()
    messages.error(request,'Blog Deleted')
    return HttpResponseRedirect("/")

def viewSingleBlog(request):
    blog_id = request.GET.get('blog_id')
    data = BlogDetails.objects.filter(id=blog_id)
    return render(request,'viewsingleblog.html',{"object":data,'blog_id':blog_id})








    