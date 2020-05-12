from django.shortcuts import render
import konna_web.delfi.delfi_random_anon_comment as drac


def index(request):
    random_comment, article_name = drac.random_comment()
    context = {
        "content": random_comment["content"].strip(),
        "author": random_comment["subject"].strip(),
        "article_name": article_name,
    }
    return render(request, "index.html", context)
