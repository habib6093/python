# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import post
from django.http import HttpResponse
from django.shortcuts import redirect
#from .form import new_posts
#from .decorators.csrf import csrf_exempt



# Create your views here.


def home(request):
    allpost=post.objects.all()
    posts=post.objects.all()
    print("the type is:..............",type(allpost))
    return render(request,'index.html',{'allpost':posts})









def post_view(request, post_no):
    postl=post.objects.get(pk=post_no)

    return render(request, 'post_view.html', {'box' : postl})







def delete_post(request, post_no):
    post.objects.get(pk=post_no).delete()

    return HttpResponse("deleted")









def new_post(request):
    if request.method == 'POST':


        titlm=request.POST.get('title')
        posm=request.POST.get('post')
        print("the result is........",posm)
        obj=post(title=titlm,description=posm)
        obj.save()
        return redirect("http://127.0.0.1:8000/home/")
        #return HttpResponse("new post successfully added")







def edit(request,post_no):
    ob=post.objects.get(pk=post_no)
    return render(request, 'edit.html', {'obs' : ob})





def update(request,post_no):
    print("post no is: ",post_no)
    ob=post.objects.get(pk=post_no)
    print("hello there i entered into update.........////////////////////")

    if request.method == 'POST':
        print("hello enterd into post .............................///////////////////")
        titlem=request.POST.get('title')
        postm=request.POST.get('post')
        print("got the values .............................///////////////////")
        ob.title=titlem
        ob.description=postm
        print("initialized .............................///////////////////")
        ob.save()
        print("saved .............................///////////////////")
        return redirect("http://127.0.0.1:8000/home/")