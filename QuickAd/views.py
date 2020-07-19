from django.shortcuts import render
#from django.contrib.auth.models import User
from django_private_chat.models import Dialog
from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from accounts.models import User
from djstripe.models import Product
import djstripe
import stripe

def get_users_dialog(dialog):
    dialog  = User.objects.get(id=dialog.opponent_id)


@login_required(login_url='/login/')
def user_dialogs(request):
    dialogs_list = Dialog.objects.filter(Q(owner_id=request.user.id) | Q(opponent_id=request.user.id))
    print(dialogs_list)
    profiles = apps.get_model('accounts', 'User')
    opponents_profiles = [(profiles.objects.get(id=dialog.opponent_id if dialog.opponent_id != request.user.id else dialog.owner_id),
                           User.objects.get(id=dialog.opponent_id if dialog.opponent_id != request.user.id else dialog.owner_id))
                          for dialog in dialogs_list]
    print(opponents_profiles)
    return render(request, 'users/dialogs_list.html', context={'opponents': opponents_profiles})
    
    
def checkout(request):
	products = Product.objects.all()
	return render(request,"checkout.html",{"products": products})
	
	
def create_sub(request):
	if request.method == 'POST':
	    # Reads application/json and returns a response
	    data = json.loads(request.body)
	    payment_method = data['payment_method']
	    stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY

	    payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
	    djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)


	    try:
	        # This creates a new Customer and attaches the PaymentMethod in one API call.
	        customer = stripe.Customer.create(
	            payment_method=payment_method,
	            email=request.user.email,
	            invoice_settings={
	                'default_payment_method': payment_method
	            }
	        )

	        djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
	        request.user.customer = djstripe_customer
	       

	        # At this point, associate the ID of the Customer object with your
	        # own internal representation of a customer, if you have one.
	        # print(customer)

	        # Subscribe the user to the subscription created
	        subscription = stripe.Subscription.create(
	            customer=customer.id,
	            items=[
	                {
	                    "price": data["price_id"],
	                },
	            ],
	            expand=["latest_invoice.payment_intent"]
	        )

	        djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

	        request.user.subscription = djstripe_subscription
	        request.user.save()

	        return JsonResponse(subscription)
	    except Exception as e:
	        return JsonResponse({'error': (e.args[0])}, status =403)
	else:
		return HTTPresponse('requet method not allowed')
		
		
		
def complete(request):
	return render(request, "complete.html")
	
	
	
	
	
	
	
	
