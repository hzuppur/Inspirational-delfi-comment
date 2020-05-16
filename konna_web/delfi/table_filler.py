from konna_web.models import Article, Comment, CommentReply
import konna_web.delfi.delfi_articles as da
import konna_web.delfi.delfi_comments as dc


def add_articles_to_table():
  # Get all delfi front page articles and iterate over them
  articles = da.get_front_page_articles()
  for d_article in articles:
    # Create new article and save it to the db
    article = Article(id=d_article["id"], name=d_article["name"], url=d_article["url"], comments=d_article["comments"])
    article.save()
    # Get all comments for that article and iterate over them
    comments = dc.get_comments_with_replies(d_article["id"])
    for d_comment in comments:
      # Check if comment has content and subject and save comment
      if d_comment["subject"] is not None and d_comment["content"]:
        comment = Comment(article=article, content=d_comment["content"], subject=d_comment["subject"])
        comment.save()
        # If comment has reply´s, add them to the reply table
        if d_comment["replies"] is not None:
          for d_reply in d_comment["replies"]:
            reply = CommentReply(comment=comment, content=d_reply["content"], subject=d_reply["subject"])
            reply.save()
