from django.shortcuts import render
from django.db.models import Q
from core.models import Ad

def searchposts(request):
    if request.method == 'GET':
        
        location = request.GET.get('location', '')
        year = request.GET.get('year', '')
        make = request.GET.get('make', '')
  
        submitbutton= request.GET.get('submit')

        if location is not None:
            lookups= (Q(location__icontains=location) | (Q(year__exact=year) | Q(make__exact=make)))

            results= Ad.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'listings.html', context)

        else:
            return render(request, 'listings.html')

    else:
        return render(request, 'listings.html')

