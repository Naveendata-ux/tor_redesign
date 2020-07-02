from django.views.generic import ListView
from django.shortcuts import render

from core.models import *
from core.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class IndexView(ListView):
    template_name = "index.html"
    model = Ad
    context_object_name = "ads"

    def get_queryset(self):
        return self.model.objects.select_related("user").select_related("category").order_by("-created_at")[:6]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['featured_products'] = Ad.objects.filter(featured=True)
        return context


class ListingListView(ListView):
    model = Ad
    template_name = "listings.html"
    context_object_name = "ads"
    
        
    def get_queryset(self):
        return self.model.objects.select_related("category").filter(status=1)
        
def about_page_view(request):
    return render(request, 'about.html')

def contact(request):
    template = 'contact.html'
    registered = False
    if request.method== 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request,"We have received your Information")
            messages.success(request,"We will contact you soon...")
            registered = True
            return render(request, 'contactmessage.html', {})
            #return render(request, 'signup/contactmessage.html')
        else:
            print(contact.errors)
    else:
        contact = ContactForm()
    return render(request, template,{'contact': contact})
    
def helpsupport_page_view(request):
    return render(request, 'help.html')

def faqs_page_view(request):
    return render(request, 'faqs.html')
 
def privacy_policy_view(request):
    return render(request, 'privacypolicy.html') 
    
def terms_of_service_view(request):
    return render(request, 'termsofservice.html') 
