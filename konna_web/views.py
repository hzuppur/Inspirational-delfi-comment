from django.shortcuts import render
import konna_web.delfi_random_anon_comment as drac

def index(request):
    random_comment = drac.random_comment()
    context = {
        'comment': random_comment,
               }
    return render(request, 'index.html', context)
