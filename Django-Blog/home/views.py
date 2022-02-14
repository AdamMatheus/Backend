from tkinter import E
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy,reverse
from home.forms import BlogForm
from .models import BlogModel,Like, Comment
from .forms import *
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.http import HttpResponseRedirect


def post_view(request):
    blogs=BlogModel.objects.all()
    user=request.user
    
    context={
        'blogs':blogs,
        'user':user,
    }
    
    return render(request,'home/home.html',context) 

def LikeView(request, pk):
	blog = get_object_or_404(BlogModel, id=request.POST.get('blog_id'))
	liked = False
	if blog.likes.filter(id=request.user.id).exists():
		blog.likes.remove(request.user)
		liked = False
	else:
		blog.likes.add(request.user)
		liked = True
	
	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


def logout_view(request):
    logout(request)
    return redirect('/')


def home(request):
    context={'blogs' : BlogModel.objects.all()}
    return render(request,'home.html',context)


def login_view(request):
    return render(request,'login.html')

def blog_detail(request,slug):
    context={}
    try:
        blog_obj= BlogModel.objects.filter(slug=slug).first()
        context['blog_obj']= blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html',context)

def see_blog(request):
    context={}
    
    try:
        blog_objs= BlogModel.objects.filter(user=request.user)
        context['blog_objs']= blog_objs
    except Exception as e:
        print(e)
    return render(request,'see_blog.html',context)

def add_blog(request):
    context={'form':BlogForm}
    try:
        if request.method =="POST":
            form =BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES ['image']
            title = request.POST.get('title')
            user =request.user
            
            if form.is_valid():
                content=form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(
                user=user,
                title =title,
                content =content,
                image =image
            )
            print(blog_obj)
            return redirect('/add-blog/')
            
    except Exception as e :
        print(e)
    return render(request,'add_blog.html',context)


def blog_update(request, slug):
    context={}
    try:
        
        
        blog_obj= BlogModel.objects.get(slug=slug)
        
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        initial_dict={'content':blog_obj.content}
        form=BlogForm(initial=initial_dict)
        if request.method =="POST":
                form =BlogForm(request.POST)
                print(request.FILES)
                image = request.FILES ['image']
                title = request.POST.get('title')
                user =request.user
                
                if form.is_valid():
                    content=form.cleaned_data['content']
                
                blog_obj = BlogModel.objects.create(
                    user=user,
                    title =title,
                    content =content,
                    image =image
                )
           
        
        
        context['blog_obj']=blog_obj
        context['form']=form
    except Exception as e:
        print(e)
        
    return render(request,'update_blog.html',context)


def blog_delete(request, slug):
    context={}
    try:
        blog_obj= BlogModel.objects.get(slug=slug)
        if blog_obj.user != request.user:
            return redirect('/')
        
        
        context['blog_obj']=blog_obj
    except Exception as e:
        print(e)
        
    return render(request,'update_blog.html',context)


def register_view(request):
    return render(request,'register.html')

def verify(request,token):
    try:
        profile_obj=Profile.objects.filter(token=token).first()
        
        if profile_obj:
            profile_obj.is_verified=True
            profile_obj.save()
        return redirect('/login/')
    
    except Exception as e:
        print (e)
        
    return redirect('/')


class AddCommentView(CreateView):
    model= Comment
    form_class=CommentForm
    template_name='add_comment.html'
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')

