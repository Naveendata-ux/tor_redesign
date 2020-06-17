from django.shortcuts import render
from django.db.models import Q
from core.models import Ad

def searchposts(request):
    if request.method == 'GET':
        
        location = request.GET.get('Location', '')
        year = request.GET.get('year', '')
        make = request.GET.get('make', '')
  
        submitbutton= request.GET.get('submit')

        if year  and make is not None:
            lookups= ((Q(Year__icontains=year) | Q(Make__icontains=make)))

            results= Ad.objects.filter(lookups).distinct()
            

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search/results.html', context)

        else:
            return render(request, 'search/results.html')

    else:
        return render(request, 'search/results.html')

