from django.shortcuts import render
from django.db.models import Q
from core.models import Ad

def searchposts(request):
    if request.method == 'GET':
        
        location = request.GET.get('location', '')
        year = request.GET.get('year', '')
        make = request.GET.get('make', '')
        
        submitbutton= request.GET.get('submit')

        if location and year  and make is not None:
            lookups= (Q(location__icontains=location) & Q(Year__icontains=year) | Q(Make__icontains=make))

            results= Ad.objects.filter(lookups).distinct()
            

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'search/results.html', context)

        else:
            return render(request, 'search/results.html')

    else:
        return render(request, 'search/results.html')
            
def index(request):

    ads = Ad.objects.all()

    # if user need to filter products otherwise list all products
    
    if request.method == "POST":
        
        # Filter criteria
        ad_title = request.POST.get("Ad_title", None)
        
        min_price = request.POST.get("min_price", None)
        max_price = request.POST.get("max_price", None)
        
        if ad_title:
            ads = Ad.objects.filter(Ad_title__contains = Ad_title)
        if min_price:
            ads = ads.filter(price__gte = min_price)
        if max_price:
            ads = ads.filter(price__lte = max_price)
        
    context = {
        'ad_title':'list of products', 
        'ads' : ads,
        
    }
    return render(request, 'search/results.html', context)

def filter(request):
    qs = Ad.objects.all()
    categories = Category.objects.all()
    Ad_title_contains_query = request.GET.get(' Ad_title_contains')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    category = request.GET.get('category')
   
    if is_valid_queryparam( Ad_title_contains_query):
        qs = qs.filter( Ad_title__icontains=title_contains_query)

    if is_valid_queryparam(offer_price_min):
        qs = qs.filter(offer_price__gte=offer_price_min)

    if is_valid_queryparam(offer_price_max):
        qs = qs.filter(offer_price__lt=offer_price_max)

    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(categories__name=category)

    
    context = {
        'queryset': qs,
        'categories': Category.objects.all()
    }
    return render(request, "ad.html", context)


    
