from django.contrib import messages, auth
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView
from .forms import *
from django.template.response import TemplateResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from django.contrib import messages
from django.contrib.auth.models import Group


def signup(request):
    registered = False

    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
       
        if form.is_valid() :
            user = form.save()
            user.set_password(user.password)
            user.save()
            group = form.cleaned_data['group']        
            group.user_set.add(user)
            registered = True
            messages.success(request,"Registration Successfull")
            
            #return render(request,'accounts/register.html')
        else:
            print(form.errors)
    else:
        form = SignUpForm()
        
    return render(request,'accounts/register.html',
                          {'form':form, 
                           'registered':registered})
                           
                           

class LoginView(FormView):
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'accounts/login.html'

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request,*args,**kwargs)

    # @method_decorator(sensitive_post_parameters('password'))
    # @method_decorator(csrf_protect)
    # @method_decorator(never_cache)
    # def dispatch(self, request, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         redirect_to = self.get_success_url()
    #         return HttpResponseRedirect(redirect_to)
    #     # return super().dispatch(self.request, *args, **kwargs)
    #     return super(Login, self).dispatch(request, *args, **kwargs)

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self,form):
        #return redirect('accounts:login')
        return self.render_to_response(self.get_context_data(form=form))
        

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    
class InsuranceInfoView(LoginRequiredMixin, TemplateView):
    questions_form = QuestionsForm
    template_name = 'users/insurance.html'
    
    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None
        
        questions_form = QuestionsForm(post_data, file_data, instance=request.user)
        
        if questions_form.is_valid() :
            questions_form.save()
            messages.success(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('accounts:profile'))

        context = self.get_context_data(questions_form=questions_form,)

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    address_form = AddressForm
    #questions_form = QuestionsForm
    template_name = 'users/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user)
        address_form = AddressForm(post_data, file_data, instance=request.user)
        #questions_form = QuestionsForm(post_data, file_data, instance=request.user)
        
        if user_form.is_valid() and profile_form.is_valid() and address_form.is_valid()  :
            user_form.save()
            profile_form.save()
            address_form.save()
            #questions_form.save()
            
            
            messages.success(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('accounts:profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form,
                                        address_form=address_form,
                                        #questions_form=questions_form,
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy('core:home')

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)
