from django.shortcuts import render, get_object_or_404
import konna_web.delfi.delfi_random_anon_comment as drac
from konna_web.models import Article, Comment


def index(request):
    random_comment, article_name, article_link = drac.random_comment()
    context = {
        "content": random_comment["content"].strip(),
        "author": random_comment["subject"].strip(),
        "article_name": article_name,
        "article_link": article_link,
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
