from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, WatchForm
from django.contrib import messages

# Create your views here.

def WatchCreateView(request):
    form = WatchForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        watch = form.cleaned_data.get('watch')
        messages.success(request, f'Watch Word set to "{watch}"')
        return redirect('post-watch')
    context = {'form':form}
    return render(request, "post/set-watch.html", context)


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'post/home.html', context)

# List of recent Posts
class PostListView(ListView):
    model = Post
    template_name = 'post/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

# Detailed View of Post
class PostDetailView(DetailView):
    model = Post

# Create a New Post
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Updaet a Post
class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Delete a Post
class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post

    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
