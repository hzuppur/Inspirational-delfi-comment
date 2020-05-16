from django.db import models


class Article(models.Model):
  id = models.IntegerField(primary_key=True)
  name = models.CharField(max_length=500)
  url = models.CharField(max_length=500)
  comments = models.IntegerField()

  def __str__(self):
    return self.name


class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE)
  content = models.CharField(max_length=4000)
  subject = models.CharField(max_length=500)

  def __str__(self):
    return self.content


class CommentReply(models.Model):
  comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
  content = models.CharField(max_length=4000)
  subject = models.CharField(max_length=500)

  def __str__(self):
    return self.content
