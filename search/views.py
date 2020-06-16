from django.shortcuts import render
from django.db.models import Q
from core.models import Ad

def searchposts(request):
    if request.method == 'GET':
        
        location = request.GET.get('Location', '')
        year = request.GET.get('year', '')
        make = request.GET.get('make', '')
  
        submitbutton= request.GET.get('submit')

        if location is not None:
            lookups= ((Q(Year__exact=year) | Q(Make__exact=make)))

            results= Ad.objects.filter(lookups).distinct()
            

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search/results.html', context)

        else:
            return render(request, 'search/results.html')

    else:
        return render(request, 'search/results.html')

