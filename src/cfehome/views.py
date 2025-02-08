from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit



def home_view(request,*args, **kwargs):
    # qs = PageVisit.obje
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    PageVisit.objects.create(path=request.path)
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    my_title = "My Page"

    try:
        percent = (page_qs.count()*100)/qs.count()
        percent = percent.__round__()

    except:
        percent = 0
    my_context = {
        "page_title":my_title,
        #  "page_title":my_title,
        "page_visit_count":page_qs.count(),
        "total_visits":qs.count(),
        "percent":percent
    }

    print("page visit count: ",page_qs.count())
    html_template = "about.html"
    return render(request,html_template,my_context)