from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import BlogModel

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
        blog_obj.delete()
    except Exception as e:
        print(e)
    return redirect('/see-blog/')



def blog_update(request, title):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(title=title)
        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)

        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                image = form.cleaned_data['image']
                updated_title = request.POST.get('title')
                user = request.user
                content = form.cleaned_data['content']
                
                blog_obj.title = updated_title
                blog_obj.content = content
                blog_obj.image = image
                blog_obj.save()
                
                return redirect('/add-blog/')

        context['blog_obj'] = blog_obj 
        context['form'] = form

    except Exception as e:
        print(e)    
    
    return render(request, 'update_blog.html', context)



