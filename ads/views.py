from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .forms import *
from core.mixins import CustomLoginRequiredMixin
from core.models import *
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import AdFilter,AdFilterServices,AdFilterWheels
from django.contrib.auth.decorators import login_required


# import the wonderful decorator
#from djstripe.decorators import subscription_payment_required

# import method_decorator which allows us to use function
# decorators on Class-Based View dispatch function.
#from django.utils.decorators import method_decorator



class AdDetailsView(DetailView):
    template_name = "ads/add_details.html"
    model = Ad
    slug_field = "id"
    slug_url_kwarg = "ad_id"
    context_object_name = "ad"
    
    
    def get_queryset(self):
        return self.model.objects.select_related("category").select_related("user").all()

    def get_context_data(self, **kwargs):
        context = super(AdDetailsView, self).get_context_data(**kwargs)
        context['ads'] = Ad.objects.select_related("user").select_related("category").order_by("-created_at")[:4]
        return context



class AdCreateView(CustomLoginRequiredMixin, CreateView):
    template_name = 'ads/create.html'
    form_class = AdCreateForm
    success_url = reverse_lazy('users:dashboard')

    def get_context_data(self, **kwargs):
        context = super(AdCreateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AdCreateView, self).form_valid(form)
    
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            # print(self.request.FILES.getlist('image'))
            self.form_valid(form)
            files = self.request.FILES.getlist('image')
            for image in files:
                photo = AdImage(ad=self.object, image=image)
                photo.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)

class AdCreateViewWheels(CustomLoginRequiredMixin, CreateView):
    template_name = 'ads/wheels.html'
    form_class = WheelCreateForm
    success_url = reverse_lazy('users:dashboard')

    def get_context_data(self, **kwargs):
        context = super(AdCreateViewWheels, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AdCreateViewWheels, self).form_valid(form)
    
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            # print(self.request.FILES.getlist('image'))
            self.form_valid(form)
            files = self.request.FILES.getlist('image')
            for image in files:
                photo = AdImage(ad=self.object, image=image)
                photo.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)


class AdCreateViewServices(CustomLoginRequiredMixin, CreateView):
    template_name = 'ads/services.html'
    form_class = ServicesCreateForm
    success_url = reverse_lazy('users:dashboard')

    def get_context_data(self, **kwargs):
        context = super(AdCreateViewServices, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AdCreateViewServices, self).form_valid(form)
    
    
    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            # print(self.request.FILES.getlist('image'))
            self.form_valid(form)
            files = self.request.FILES.getlist('image')
            for image in files:
                photo = AdImage(ad=self.object, image=image)
                photo.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.form_invalid(form)



class AdUpdateView(CustomLoginRequiredMixin, UpdateView):
    model = Ad
    template_name = "ads/edit.html"
    context_object_name = "ad"
    slug_field = "id"
    slug_url_kwarg = "ad_id"
    form_class = AdUpdateForm
    success_url = reverse_lazy("users:dashboard")

    def get_queryset(self):
        return self.model.objects.select_related("category").filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(AdUpdateView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        ad = form.save(commit=True)
        files = self.request.FILES.getlist('image')
        if len(files):
            AdImage.objects.filter(ad=self.object).delete()
            for image in files:
                photo = AdImage(ad=self.object, image=image)
                photo.save()
        messages.success(self.request, "Ad successfully updated")
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        obj = self.model.objects.get(id=self.kwargs['ad_id'])
        #obj = self.model.objects.select_related('AdImage').filter(id=self.kwargs['ad_id'])
        if obj is None:
            raise Http404("Ad doesn't exists")
        return obj

    def get_images(self, queryset=None):
        adobj = self.model.objects.get(ad=self.kwargs['ad_id'])
        if adobj is None:
            raise Http404("No images for this ad ")
        return adobj




class AdDeleteView(DeleteView):
    model = Ad
    slug_field = "id"
    slug_url_kwarg = "ad_id"
    success_url = reverse_lazy('users:dashboard')

    def get_queryset(self):
        return self.model.objects.select_related("category").filter(user=self.request.user)

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(AdDeleteView, self).get_object()
        if not obj.user == self.request.user:
            raise Http404
        return obj
        
def post_ad_view(request):
    return render(request, 'ads/select_category.html')
           
def tyresad(request):
    # if this is a POST request we need to process the form data
    template = 'ads/tyres.html'
    
    def get_context_data(self, **kwargs):
        context = super(tyresad, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    if request.method == 'POST':
        
        #form = TyresForm(request.POST)
        tyres = TyresForm(request.POST)
        ad = AdCreateForm(request.POST)
        
        if tyres.is_valid() and ad.is_valid():
                tyres.save()
                ad.save()
                files = self.request.FILES.getlist('image')
                for image in files:
                    photo = AdImage(ad=self.object, image=image)
                    photo.save()
                # redirect to accounts page:
                return render(request, 'users/dashboard.html')
                #redirect('index')
        else:
            print(tyres.errors,ad.errors)

   # No post data availabe, let's just show the page.
    else:
        tyres = TyresForm()
        ad=AdCreateForm()
        #form = TyresForm()

    return render(request, template, {'tyres': tyres,'ad':ad})

def wheelsad(request):
    # if this is a POST request we need to process the form data
    template = 'ads/wheels.html'
   
    if request.method == 'POST':
        
        wheels = WheelsForm(request.POST)
        ad = AdCreateForm(request.POST)
        
        if wheels.is_valid() and ad.is_valid():
                
                wheels.save()
                ad.save()
                files = request.FILES.getlist('image')
                for image in files:
                    photo = AdImage(ad=self.object, image=image)
                    photo.save()
           
                return render(request, 'users/dashboard.html')
        else:
            print(wheels.errors,ad.errors)

   # No post data availabe, let's just show the page.
    else:
        wheels  = WheelsForm()
        ad = AdCreateForm()

    return render(request, template, {'wheels': wheels,'ad':ad})
    

def ad_favourite_list(request):

    user = request.user
    favorite_ads = user.favourite.all()
    
    return render(request, 'ads/favourite_list.html')

def favourite_ad(request, id):
    ad = get_object_or_404(Ad, id=id)
    if ad.favourite.filter(id=request.user.id).exists():
        ad.favourite.remove(request.user)
    else:
        ad.favourite.add(request.user)
    return HttpResponseRedirect(ad.get_absolute_url())



    
def filter(request):
    ad_filter = AdFilter(request.GET, queryset=Ad.objects.all())
    page = request.GET.get('page')
    paginator = Paginator(ad_filter.qs, 4)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {'filter': ad_filter, 'ads': ads}
    return render(request, 'ads/filter.html', context)

def filter_wheels(request):
    ad_filter_wheels = AdFilterWheels(request.GET, queryset=Ad.objects.all())
    page = request.GET.get('page')
    paginator = Paginator(ad_filter_wheels.qs, 4)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {'filter': ad_filter_wheels, 'ads': ads}
    return render(request, 'ads/filter_wheels.html', context)


def filter_services(request):
    ad_filter_services = AdFilterServices(request.GET, queryset=Ad.objects.all())
    page = request.GET.get('page')
    paginator = Paginator(ad_filter_services.qs, 4)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {'filter': ad_filter_services, 'ads': ads}
    return render(request, 'ads/filter_services.html', context)



def search(request):
    queryset = Ad.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    ad_filter = AdFilter(request.GET, queryset=Ad.objects.all())

    if query:
        queryset = queryset.filter(Q(Ad_title__icontains=query) | Q(category__icontains=query) |
                                   Q(offer_price__icontains=query) ).distinct()
    page = request.GET.get('page')
    paginator = Paginator(queryset, 12)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {'queryset': queryset,
               'filter': ad_filter,
               'ads': ads,
               'q': query}
    return render(request, 'ads/search.html', context)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
