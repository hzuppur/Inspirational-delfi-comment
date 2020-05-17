from django.shortcuts import render, get_object_or_404
from konna_web.models import Article, Comment
import konna_web.delfi.database_utils as db_util


def index(request):
    random_comment, article = db_util.get_random_comment()
    context = {
        "content": random_comment.content.strip(),
        "author": random_comment.subject.strip(),
        "article_name": article.name,
        "article_link": article.url,
    }
    return render(request, "index.html", context)

def articles(requests):
    context = {"articles": Article.objects.order_by("comments").reverse(),}
    return render(requests, "articles.html", context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
        'comments': article.comment_set.all().prefetch_related('commentreply_set'),
    }

    return render(request, 'detail.html', context)
