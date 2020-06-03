from django.contrib import messages
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from .forms import *
from core.mixins import CustomLoginRequiredMixin
from core.models import *
from django.shortcuts import render,redirect

def ad_select_type(request):
    """View for add ad modal embedded in the product list view."""
    form = forms.AdTypeSelectorForm(request.POST or None)
    status = 200
    if form.is_valid():
        redirect_url = reverse(
            "ads:crate.ad",
            kwargs={"type_pk": form.cleaned_data.get("ad_type").pk},
        )
        return (
            JsonResponse({"redirectUrl": redirect_url})
            if request.is_ajax()
            else redirect(redirect_url)
        )
    elif form.errors:
        status = 400
    ctx = {"form": form}
    template = "index.html"
    return TemplateResponse(request, template, ctx, status=status)



class AdDetailsView(DetailView):
    template_name = "ads/add_details.html"
    model = Ad
    slug_field = "id"
    slug_url_kwarg = "ad_id"
    context_object_name = "ad"

    def get_queryset(self):
        return self.model.objects.select_related("category").select_related("user").all()


class AdCreateView(CustomLoginRequiredMixin, CreateView):
    template_name = 'ads/create.html'
    form_class = AdCreateForm
    success_url = reverse_lazy('accounts:login')

   # def get_context_data(self, **kwargs):
        #context = super(AdCreateView, self).get_context_data(**kwargs)
        #context['categories'] = Category.objects.all()
        #return context
    
    #def get_context_data(self, **kwargs):
     #   context = super(AdCreateView, self).get_context_data(**kwargs)
      #  context['attributes'] = Attribute.objects.all()
       # return context
 

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
        if obj is None:
            raise Http404("Ad doesn't exists")
        return obj


class AdDeleteView(DeleteView):
    model = Ad
    slug_field = "id"
    template_name = "ads/ad_delete_confirm.html"
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
   
    if request.method == 'POST':
        
        #form = TyresForm(request.POST)
        tyres = TyresForm(request.POST)
        ad = AdCreateForm(request.POST)
        
        if tyres.is_valid() and ad.is_valid():
                tyres.save()
                ad.save()
               
                # Login the user
                #login(request, user)
               
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
                # Login the user
                #login(request, user)
               
                # redirect to accounts page:
                #return HttpResponseRedirect('/tyres/postmsg')
           
                return render(request, 'users/dashboard.html')
        else:
            print(wheels.errors,ad.errors)

   # No post data availabe, let's just show the page.
    else:
        wheels  = WheelsForm()
        ad = AdCreateForm()

    return render(request, template, {'wheels': wheels,'ad':ad})
