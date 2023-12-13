# Models for the blog app

from django.db import models
from django.contrib.auth.models import User

# Represents blog posts
class Post(models.Model):
    # Title with max length of 255
    title = models.CharField(max_length=255)
    # Textfield for post content
    content = models.TextField()
    # Date time field for post
    date_posted = models.DateTimeField(auto_now_add=True)
    # Foreign key linking user to post
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def user_has_liked(self, user):
        return self.like_set.filter(user=user).exists()

# Represents comments left underneath a blog post
class Comment(models.Model):
    # Text content of comment
    content = models.TextField()
    # Date time field for post
    date_posted = models.DateTimeField(auto_now_add=True)
    # Link foreign key of post to comment
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Link foreign key of user to comment
    author = models.ForeignKey(User, on_delete=models.CASCADE)

# Represents a like left on a blog post
class Like(models.Model):
    # Link foreign key to post, show it was liked
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # Link foreign key to user, show who liked it
    user = models.ForeignKey(User, on_delete=models.CASCADE)