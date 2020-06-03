from django.shortcuts import render
from django.db.models import Q
from core.models import Ad, Tyres

def searchposts(request):
    if request.method == 'GET':
        
        location = request.GET.get('location', '')
        year = request.GET.get('year', '')
        make = request.GET.get('make', '')
  
        submitbutton= request.GET.get('submit')

        if location is not None:
            lookups= ((Q(Year__exact=year) | Q(Make__exact=make)))

            results= Tyres.objects.filter(lookups).distinct()
            

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'listings.html', context)

        else:
            return render(request, 'listings.html')

    else:
        return render(request, 'listings.html')

