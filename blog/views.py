from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import BlogModel
from django.contrib.auth import logout 

def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def blog_detail(request, title):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(title = title).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

def see_blog(request):
    context = {}
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)
    return render(request, 'see_blogs.html', context)

def add_blog(request):
    form = BlogForm()
    context = {'form': form}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
            
            if form.is_valid():
                content = form.cleaned_data['content']
                blogobj = BlogModel.objects.create(user=user, title=title, content=content, image=image)
                print("aryan")
                return redirect('/add-blog/')

    except Exception as e:
        print(e)
    return render(request, 'add_blog.html', context)


def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)
        
        if blog_obj.user != request.user:
            return redirect('/')

        blog_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/see-blog/')


def blog_update(request, title):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(title=title)

        if blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)

        if request.method == 'POST':
            form = BlogForm(request.POST)
        if form.is_valid():
            image = request.FILES['image']
            title = request.POST.get('title')
            content = form.cleaned_data['content']
            
            blog_obj.title = title
            blog_obj.content = content
            blog_obj.image = image
            blog_obj.save()

            return redirect('/add-blog/')

        context['blog_obj'] = blog_obj 
        context['form'] = form

    except Exception as e:
        print(e)    
    
    return render(request, 'update_blog.html', context)

def logout_view(request):
    logout(request)
    return redirect('/')