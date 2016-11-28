from django.shortcuts import render_to_response, render, get_object_or_404
from .models import Post
from django.template import RequestContext
from .forms import *
from blog.forms import AddPostForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, logout, login as django_login
#from django.bing_search import run_query

def post_list(request):
    posts = Post.objects.all().filter(is_published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})


def index(request):
    return render(request, 'blog/index.html', {})


def about(request):
    return render(request, 'blog/about.html', {})


def team(request):
    return render(request, 'blog/teampair.html', {})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            django_login(request, user)
            return HttpResponseRedirect('/')

    form = LoginForm()
    return render(request, 'blog/login.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'], email=form.cleaned_data['email'])
            user.save()
            return HttpResponseRedirect('/')
    form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')


def addPost(request):
    if request.method == 'POST':
        post_form = AddPostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save()
            return HttpResponseRedirect('/')
        else:
            print('There is an error in your form')
    else:
        post_form = AddPostForm()
    return render(request, 'blog/add_post.html', {'post_form': post_form})


def reviewPost(request):
    if request.method == 'POST':
        if 'Approve' in request.POST:
            print ('approve')
        else:
            pass
    posts = Post.objects.all().filter(is_published=False)
    return render(request, 'blog/reviewnewposts.html', {'posts': posts})


def approvePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.is_published = True
    post.save()
    print ('Post ID: ', post_id)
    return HttpResponseRedirect('/')

def search(request):
    context = RequestContext(request)
    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            # Run our Bing function to get the results list!
            result_list = SearchForm()

    return render_to_response('django/search.html', {'result_list': result_list})







