from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Like

# List all blog posts ordered by the date they were posted
def blog_list(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {'posts': posts}
    return render(request, 'list.html', context)

# Create a new blog post
@login_required
def create_post(request):
    if request.method == 'POST':
        # Get the title and content from the POST data
        title = request.POST['title']
        content = request.POST['content']
        # Create a new post with the title, content, and the user who made the request
        post = Post.objects.create(title=title, content=content, author=request.user)
        return HttpResponseRedirect(reverse('blog:blog_list'))
    else:
        context = {}
        return render(request, 'create_post.html', context)

# Display the details of a specific blog post
def post_detail(request, post_id):
    # Get the post with the given id, or raise a 404 error if it doesn't exist
    post = get_object_or_404(Post, id=post_id)
    comments = post.comment_set.order_by('-date_posted')
    user_has_liked = post.user_has_liked(request.user)
    context = {'post': post, 'comments': comments, 'user_has_liked': user_has_liked}
    return render(request, 'post_detail.html', context)

# Add comment to a specific blog post
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST['content']
        # Create a new comment with the content, the user who made the request and the post
        comment = Comment.objects.create(post=post, content=content, author=request.user)
        return HttpResponseRedirect(reverse('blog:post_detail',args=(post.id,)))
    else:
        return HttpResponseRedirect(reverse('blog:post_detail',args=(post.id,)))

# Allows user to like a specific blog post
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'GET':
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            # If a new like was created, redirect the user to the post detail page
            return HttpResponseRedirect(reverse('blog:post_detail',args=(post.id,)))
        else:
            # If the like already exists, delete it and redirect the user to the post detail page
            like.delete()
            return HttpResponseRedirect(reverse('blog:post_detail',args=(post.id,)))
    else:
        return HttpResponseRedirect(reverse('blog:post_detail',args=(post.id,)))