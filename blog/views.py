from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View

from .models import Post
from .forms import CommentForm

# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


class SinglePostView(View):
    
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": CommentForm()
        }
        return render(request, "blog/post-detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)  #take input from the form
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
          comment = comment_form.save(commit=False) #creates a new model instance in the database
          comment.post = post #adds extra data
          comment.save()  #and saves the data back to database
          
          return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))

        context = {
          "post": post,
          "post_tags": post.tags.all(),
          "comment_form": comment_form
        }
        return render(request, "blog/post-detail.html", context)