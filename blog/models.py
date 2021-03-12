from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    link = models.URLField(max_length = 400)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Connect(models.Model):
    email_id = models.CharField(max_length=200)
    twitter_id = models.CharField(max_length=200)
    linkedin_id = models.CharField(max_length=200)
    insta_id = models.CharField(max_length=200)
    twitter_link = models.URLField(max_length = 400)
    linkedin_link = models.URLField(max_length = 400)
    insta_link = models.URLField(max_length = 400)
    email_content = models.TextField(null=True)
    twitter_content = models.TextField()
    linkedin_content = models.TextField()
    insta_content = models.TextField()
