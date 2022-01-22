from django import forms
from account_app.models import Account,Referral

from users_app.models import Transactions,Notification,Investments,Packages


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = "__all__"



class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"



class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investments
        fields = "__all__"



class PackagesForm(forms.ModelForm):
    class Meta:
        model = Packages
        fields = "__all__"



class TransactionsForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = "__all__"


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"