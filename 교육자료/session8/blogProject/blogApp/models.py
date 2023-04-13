from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=50)
    dt = models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()

    def __str__(self):
        return self.content
    
class Re_comment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='re_comments')
    content = models.TextField()

    def __str__(self):
        return self.content