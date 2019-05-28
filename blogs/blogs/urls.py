"""blogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from greatx_blog_app import views
from django.views.generic import TemplateView,ListView,DetailView
from greatx_blog_app.models import Registration,BlogDetails
from blogs import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.view_blog_details,name='viewblogdetails'),
    path('registrationform/',views.registration_form,name='registrationform'),
    path('saveuserdetails/',views.save_user_details,name='saveuserdetails'),    
    path('enterblogdetails/',views.enter_blog_details,name='enterblogdetails'),
    path('saveblogdetails/',views.save_blog_details,name='saveblogdetails'),    
    path('edit/',views.edit_blog,name='editblogdetails'),
    path('editblogdetails/',views.edit_blog_details,name='editblogdetails'),
    path('delete/',views.delete_blog_details,name='deleteblogdetals'),
    path('viewsingleblog/',views.view_single_blog,name='viewsingleblog'),    
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)