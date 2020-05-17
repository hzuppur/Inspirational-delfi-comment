from konna_web.models import Article, Comment, CommentReply
import konna_web.delfi.delfi_articles as da
import konna_web.delfi.delfi_comments as dc
from django.utils import timezone
import random


def add_articles_to_table():
  # Get all delfi front page articles and iterate over them
  articles = da.get_front_page_articles()
  for d_article in articles:
    # Create new article and save it to the db
    article = Article(id=d_article["id"], name=d_article["name"], url=d_article["url"], comments=d_article["comments"], pub_date=timezone.now())
    article.save()
    # Get all comments for that article and iterate over them
    comments = dc.get_all_comments(d_article["id"], with_replies=True)

    for d_comment in comments:
      # Check if comment has content and subject and save comment
      if d_comment["subject"] is not None and d_comment["content"]:
        comment, created = Comment.objects.get_or_create(article=article, content=d_comment["content"], subject=d_comment["subject"])

      # If comment has reply´s, add them to the reply table
      if d_comment["replies"] is not None:
        for d_reply in d_comment["replies"]:
          reply, created = CommentReply.objects.get_or_create(comment=comment, content=d_reply["content"], subject=d_reply["subject"])


def remove_old_articles():
  articles = Article.objects.all()
  for article in articles:
    if not article.was_published_recently():
      article.delete()

def get_random_comment():
  comments = []
  # Loop while we get article with atleast 1 comment
  while len(comments) == 0:
    article = random.choice(Article.objects.all())
    comments.extend(article.comment_set.all())
  return random.choice(comments), article
