from django.shortcuts import render

def hello_world(request):
    return render(request, 'index.html', {})

def my_contact(request):
    return render(request, 'contact.html', {})

def my_service(request):
    return render(request, 'services.html', {})

def my_portfolio(request):
    return render(request, 'portfolio.html', {})


def my_about(request):
    return render(request, 'about.html', {})

def my_blog(request):
    return render(request, 'blog.html', {})

def my_blog_single(request):
    return render(request, 'blog_single.html', {})

