from django.shortcuts import render,redirect
from django.apps import apps
from django.contrib import  messages
from django.utils import timezone
from datetime import timedelta
from django.template.loader import render_to_string

# Create your views here.

from account_app.models import Account,Referral

from users_app.models import Transactions,Notification,Investments,Packages

from .forms import ReferralForm,AccountForm,InvestmentForm,PackagesForm,TransactionsForm,NotificationForm

from .decorators import manager_required
EMAIL_ADMIN = "worldcryptocurrencies01@gmail.com"
D =  'deposite'
W = "withdraw"



@manager_required
def index(request):
    return render(request, 'admin_app/index.html')



 

@manager_required
def list_(request,app_name,mod):
    mod_name = str(mod).capitalize()
    model = apps.get_model(f'{app_name}',f'{mod_name}')
    objects = model.objects.all()
    objects_count = model.objects.all().count()
    if request.POST:
        action = request.POST.get('action')
        if mod == "transactions":
            if action == "approve_trans":
                selected_pk = int(request.POST.get('selected_pk'))
                trans = model.objects.get(pk=selected_pk)

                trans.status = 'approved'
                trans.user.deposite_balance += trans.amount
                subject = "Transaction Approved"
                message = render_to_string('admin_app/trans-email.html', {
                'user': trans.user,
                'date': timezone.now(),
                'amount': trans.amount,
                'status': "Approved",
                'trans': trans.trans_type,
                })
                trans.user.save()
                trans.save()
                Notification.objects.create(user=trans.user,title="Transaction Approved", body=f" YOUR f{trans.trans_type} OF ${trans.amount} HAS BEEN APPROVED YOU CAN NOW BUY A PLAN")
                trans.user.email_user(subject, message)
                messages.success(request, ('Transaction Approved'))
                return redirect(f'/sadmin/users_app/transactions/')
            elif action == "decline_trans":
                selected_pk = int(request.POST.get('selected_pk'))
                trans = model.objects.get(pk=selected_pk)

                trans.status = 'declined'
                trans.user.deposite_balance += trans.amount
                subject = "Transaction Declined"
                message = render_to_string('admin_app/trans-email.html', {
                'user': trans.user,
                'date': timezone.now(),
                'amount': trans.amount,
                'status': "Declined",
                'trans': trans.trans_type,
                })
                trans.user.save()
                trans.save()
                Notification.objects.create(user=trans.user,title="Transaction Declined", body=f" YOUR f{trans.trans_type} OF ${trans.amount} HAS BEEN Declined YOU CAN CONTACT ADMIN FOR FURTHER INSTRUCTIONS")
                trans.user.email_user(subject, message)
                messages.success(request, ('Transaction Declined'))
                return redirect(f'/sadmin/users_app/transactions/')
            else:
                messages.success(request, ('Unknown Error'))
                return redirect(f'/sadmin/users_app/transactions/')
    return render(request, 'admin_app/list.html',
                    {'objects':objects,"app_name":app_name.capitalize(),"app_name_sm":app_name,"mod":mod,
                    "objects_count":objects_count,"mod_c":mod_name})



@manager_required
def edit_ref(request,app_name,pk):
    mod = "referral"
    mod_name = str(mod).capitalize()
    model = apps.get_model(f'{app_name}',f'{mod_name}')
    obj = model.objects.get(pk=pk)
    if request.POST:
        form = ReferralForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, ('Referral Updated'))
            return redirect(f"/sadmin/{app_name}/{mod}/{pk}/change/")
    else:
        form = ReferralForm(instance=obj)
    context = {
        "form" : form,
        "obj" : obj,
        'mod_sm': mod,
        'app_name_sm':app_name
    }
    return render(request, 'admin_app/edit_ref.html',context)

@manager_required
def edit_account(request,app_name,pk):
    mod = "account"
    mod_name = str(mod).capitalize()
    model = apps.get_model(f'{app_name}',f'{mod_name}')
    obj = model.objects.get(pk=pk)
    if request.POST:
        form = AccountForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, ('Account Updated'))
            return redirect(f"/sadmin/{app_name}/{mod}/{pk}/change/")
    else:
        form = AccountForm(instance=obj)
    context = {
        "form" : form,
        "obj" : obj,
        'mod_sm': mod,
        'app_name_sm':app_name
    }
    return render(request, 'admin_app/edit_acc.html',context)



@manager_required
def edit_investments(request,app_name,pk):
    mod = "investments"
    mod_name = str(mod).capitalize()
    model = apps.get_model(f'{app_name}',f'{mod_name}')
    obj = model.objects.get(pk=pk)
    if request.POST:
        form = InvestmentForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, ('Investment Updated'))
            return redirect(f"/sadmin/{app_name}/{mod}/{pk}/change/")
    else:
        form = InvestmentForm(instance=obj)
    context = {
        "form" : form,
        "obj" : obj,
        'mod_sm': mod,
        'app_name_sm':app_name
    }
    return render(request, 'admin_app/edit_invest.html',context)




@manager_required
def edit_packages(request,app_name,pk):
    mod = "packages"
    mod_name = str(mod).capitalize()
    model = apps.get_model(f'{app_name}',f'{mod_name}')
    obj = model.objects.get(pk=pk)
    if request.POST:
        form = PackagesForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, ('Package Updated'))
            return redirect(f"/sadmin/{app_name}/{mod}/{pk}/change/")
    else:
        form = PackagesForm(instance=obj)
    context = {
        "form" : form,
        "obj" : obj,
        'mod_sm': mod,
        'app_name_sm':app_name
    }
    return render(request, 'admin_app/edit_package.html',context)





@manager_required
def edit_transactions(request,app_name,pk):
    mod = "transactions"
    mod_name = str(mod).capitalize()
    model = apps.get_model(f'{app_name}',f'{mod_name}')
    obj = model.objects.get(pk=pk)
    if request.POST:
        form = TransactionsForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, ('Transaction Updated'))
            return redirect(f"/sadmin/{app_name}/{mod}/{pk}/change/")
    else:
        form = TransactionsForm(instance=obj)
    context = {
        "form" : form,
        "obj" : obj,
        'mod_sm': mod,
        'app_name_sm':app_name
    }
    return render(request, 'admin_app/edit_transaction.html',context)



def get_form(mod,post,request):
    if mod == "Transactions":
        if post == True:
            form = TransactionsForm(request.POST)
        else:
            form = TransactionsForm()
    elif mod == "Notification":
        if post == True:
            form = NotificationForm(request.POST)
        else:
            form = NotificationForm()
    elif mod == "Investments":
        if post == True:
            form = InvestmentForm(request.POST)
        else:
            form = InvestmentForm()
    elif mod == "Packages":
        if post == True:
            form = PackagesForm(request.POST)
        else:
            form = PackagesForm()
    else:
        form = None
    return form





@manager_required
def add_model(request,app_name,mod):
    mod_name = str(mod).capitalize()
    model = apps.get_model(f'{app_name}',f'{mod_name}')
    if request.POST:
        form = get_form(mod_name,True,request)
        if form.is_valid():
            instance = form.save()
            messages.success(request, (f'{mod_name} Added'))
            return redirect(f"/sadmin/{app_name}/{mod}/{instance.pk}/change/")
    else:
        form = get_form(mod_name,False,request)
    print(mod_name)
    print(form)
    context= {
        "form":form,
        'mod':mod_name
    }
    return render(request,"admin_app/add_mod.html",context)




@manager_required
def edit_notification(request,app_name,pk):
    mod = "notification"
    mod_name = str(mod).capitalize()
    model = apps.get_model(f'{app_name}',f'{mod_name}')
    obj = model.objects.get(pk=pk)
    if request.POST:
        form = NotificationForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, ('Notification Updated'))
            return redirect(f"/sadmin/{app_name}/{mod}/{pk}/change/")
    else:
        form = NotificationForm(instance=obj)
    context = {
        "form" : form,
        "obj" : obj,
        'mod_sm': mod,
        'app_name_sm':app_name
    }
    return render(request, 'admin_app/edit_notification.html',context)