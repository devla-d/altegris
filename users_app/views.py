from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import  messages
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta



from account_app.models import Account,Referral

from .models import Transactions,Notification,Investments,Packages
from .forms import UserUpdateForm,PasswordChangeForm

D =  'deposite'
W = "withdraw"

def get_deadline(h):
	return timezone.now() + timedelta(days=h)


def earnings(amount , perc): 
    p = (perc/100) * amount
    return p + amount

@login_required()
def index(request):
    deadline = False
    expected_earnings  = 0
    context = {}
    try:
        investments = Investments.objects.get(user=request.user)
        today = timezone.now()
        if today >= investments.end_date:
            deadline = True
        if investments.is_complete == True:
            deadline = False
        expected_earnings = earnings(investments.amount_invested,investments.package.percent)
        context['expected_earnings'] = expected_earnings
        context['deadline'] = deadline
        context['investments'] = investments
    except:
        investments = None
        context['investments'] = investments
    print(context)
    return render(request, 'users/dashboard.html',context)



@login_required()
def create_investment(request):
    packages = Packages.objects.all()
    user = request.user
    if request.POST:
        package_id =  int(request.POST.get('package'))
        amount = int(request.POST.get('amount'))
        package = get_object_or_404(Packages, pk=package_id)
        if user.deposite_balance >=  amount:
            if amount not in range(package.min_amount ,package.max_amount):
                messages.success(request, (f'Input Amount Between Your Selected Plans Price'))
                return redirect("create-investment")
            investment , created =  Investments.objects.get_or_create(user=user)
            investment.end_date = get_deadline(package.days)
            investment.start_date = timezone.now()
            investment.amount_invested = amount
            investment.status = 'active'
            investment.package = package
            investment.is_complete = False 
            user.deposite_balance -=  amount
            user.total_amount_invested +=  amount
            user.total_investement_count += 1
            user.save()
            investment.save()
            messages.success(request, ('YOUR INVESTMENT HAS BEEN ACTIVATED'))
            return redirect("dashboard")
        else:
            messages.success(request, ('INSUFFICIENT FUNDS,PLEASE DEPOSIT'))
            return redirect("create-investment")
    return render(request, 'users/create_investment.html',{'packages':packages})

@login_required()
def claim_investment(request):
    user = request.user
    if request.POST:
        try:
            investment = Investments.objects.get(user=user)
            expected_earnings = earnings(investment.amount_invested,investment.package.percent)
            investment.amount_earn = expected_earnings
            investment.status = 'completed'
            investment.is_complete = True
            investment.save()
            user.balance += expected_earnings
            user.save()
            messages.success(request, ('Investment Has Been Claim '))
            return redirect("dashboard")
        except:
            messages.success(request, ('SOMETHING WENT WRONG'))
            return redirect("dashboard")
    else:
        messages.success(request, ('UKNOWN ERROR OCCURED'))
        return redirect("dashboard")

@login_required()
def wallet(request):
    user = request.user
    tot_balance  = user.bonus + user.balance
    amount_earn =  user.balance - user.bonus 
    return render(request, 'users/wallet.html',{'tot_balance':tot_balance,'amount_earn':amount_earn})



@login_required()
def history(request):
    transactions = Transactions.objects.filter(user=request.user).order_by('-date')
    return render(request, 'users/history.html',{"transactions":transactions})


@login_required()
def withdraw(request):
    if request.POST:
        user = request.user
        amount = int(request.POST.get('amount'))
        coin_tpye = request.POST.get('coin')
        wallet_address = request.POST.get('wallet_address')
        if amount > user.balance:
            messages.success(request, ('Inssuficient Funds'))
            return redirect("withdraw")
        else:
            Transactions.objects.create(user= user, amount=amount,coin_tpye=coin_tpye,trans_type=W,wallet_address=wallet_address)
            user.balance -= amount
            user.save()
            messages.success(request, ('Your Withdrawal Has Been Placed'))
            return redirect("withdraw")
    return render(request, 'users/withdraw.html')


@login_required()
def deposit(request):
    if request.POST:
        user = request.user
        amount = request.POST.get('amount')
        coin_tpye = request.POST.get('coin')
        Transactions.objects.create(user= user, amount=amount,coin_tpye=coin_tpye,trans_type=D)
        messages.success(request, (f'Your Deposit Of ${amount} Has Been Made'))
        return redirect("deposit")
    return render(request, 'users/deposit.html')


@login_required()
def notification(request):
    notification = Notification.objects.filter(user=request.user).order_by('-date')
    return render(request, 'users/notification.html',{'notification':notification})


@login_required()
def settings(request):
    user = request.user
    if request.POST:
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, ('YOUR ACCOUNT HAS BEEN UPDATED'))
            return redirect("settings")
    else:
        u_form = UserUpdateForm(instance=user)
    return render(request, 'users/settings.html',{"u_form":u_form})



@login_required()
def security(request):
    user = request.user
    if request.POST:
        p_form = PasswordChangeForm(request.POST,instance=user)
        if p_form.is_valid():
            password1 = p_form.cleaned_data['password1']
            user.set_password(password1)
            user.save()
            messages.info(request, f'Password Change')
            return redirect('security')
    else:
        p_form =  PasswordChangeForm(initial={'user_id': user.id})
    return render(request, 'users/security.html',{'p_form':p_form})


@login_required()
def account(request):
    user = request.user
    tot_balance  = user.bonus + user.balance
    amount_earn =  user.balance - user.bonus
    referral = Referral.objects.get(user=user)
    return render(request, 'users/account.html',{"amount_earn":amount_earn,"referral":referral})