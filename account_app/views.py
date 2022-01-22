from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import  messages
from django.http import JsonResponse
from django.contrib.auth  import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_text
from django.urls import reverse_lazy
from django.core.mail import EmailMessage, send_mail
from django.template import Context
from django.template.loader import render_to_string, get_template






from .models import Account,Referral
from .forms import RegistrationForm,LoginForm

from .import utils







def sign_up(request):
    
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            #set user active staus to false and save
            instance.is_active = False
            instance.save()
            refferd_by_pk = request.POST.get('refferd_by')
            print(refferd_by_pk)
            #check if instance has a referral
            if refferd_by_pk:
                try:
                    #Get The User That refferd the New User
                    refferd_by = Account.objects.get(pk=int(refferd_by_pk))
                    #Get The new user Referral Model
                    new_user_ref_m = Referral.objects.get(user =instance)
                    #Asign refferd_by to new user and save
                    new_user_ref_m.recommended_by = refferd_by
                    new_user_ref_m.user.recom_user_bonus = utils.referral_bonus
                    new_user_ref_m.user.save()
                    new_user_ref_m.save()
                    #Get The Old user Referral Model
                    refferd_by_ref_m = Referral.objects.get(user =refferd_by)
                    #add new user to old-user recom ref model
                    refferd_by_ref_m.recomended_users.add(instance)
                    #increase old user referral  , bonus  and save
                    refferd_by_ref_m.user.refferal += 1
                    refferd_by_ref_m.user.bonus += utils.referral_bonus
                    refferd_by_ref_m.user.balance += utils.referral_bonus
                    refferd_by_ref_m.user.save()
                    refferd_by_ref_m.save()
                except:
                    messages.info(request, f'Something went Wrong')
                    return redirect('sign_up')



            
            current_site = get_current_site(request)
            subject = '[ALTEGRIS.COM]Confirm Your Email Address'
            context = {
                'user': instance,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(instance.pk)),
                'token': default_token_generator.make_token(instance),
                }
            message = get_template("auth/account_activation_email.html").render(context)
            mail = EmailMessage(
                subject=subject,
                body=message,
                from_email=utils.EMAIL_ADMIN,
                to=[instance.email],
                reply_to=[utils.EMAIL_ADMIN],
            )
            mail.content_subtype = "html"
            mail.send(fail_silently=True)
            
            messages.success(request, ('Please check your mail box for confirmation email'))
            return redirect("sign_up")

    else:
        form = RegistrationForm()


    if request.GET.get('ref-code'):
        print(request.GET.get('ref-code'))
        refferd_by = request.GET.get('ref-code')
        return render(request, 'auth/register.html',{"form":form , "refferd_by" : refferd_by})
    else:
        return render(request, 'auth/register.html',{"form":form})








def account_activate_view(request, uidb64, token, *args, **kwargs):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_email_verifield = True
        user.save()
        login(request, user)
        messages.success(request, ('Please Complete Your Account Setup'))
        return redirect('dashboard')
    else:
        messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
        return redirect('sign_up')





def sign_in(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    destination = get_redirect_if_exists(request) 
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            print("GOOD TO GO")
            username = request.POST['username']
            password = request.POST['password']
            destination = request.POST.get('destination')
            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                if destination:
                    return redirect(destination)
                else:
                    return redirect("dashboard")
    else:
        form = LoginForm()
    return render(request, 'auth/login.html',{"form":form,"destination":destination})



def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


def sign_out(request):
    logout(request)
    return redirect('sign_in')