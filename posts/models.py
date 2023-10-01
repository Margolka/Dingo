from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        "posts.Author", on_delete=models.CASCADE, blank=True, null=True
    )

    def __str__(self):
        return f"id:{self.id}, title={self.title}, content={self.content}, created={self.created}, modified={self.modified}"


class Author(models.Model):
    nick = models.CharField(max_length=10, unique=True)
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nick}"
