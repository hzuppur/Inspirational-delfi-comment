from django.shortcuts import render
import konna_web.delfi.delfi_random_anon_comment as drac


def index(request):
    random_comment, article_name = drac.random_comment()
    context = {
        "comment": random_comment.strip(),
        "article_name": article_name.strip(),
    }
    return render(request, "index.html", context)
