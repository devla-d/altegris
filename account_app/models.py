from django.db import models 
from django.contrib.auth.models import AbstractUser
from django.conf import settings 

 
#from uuid import uuid4






class Account(AbstractUser):
    email       = models.EmailField(verbose_name='email', max_length=60, unique=True )
    zipcode    = models.CharField(max_length=30,blank=True,null=True)
    country    = models.CharField(max_length=100,blank=True,null=True)
    fullname    = models.CharField(max_length=100,blank=True,null=True)
    
    address    = models.CharField(max_length=100,blank=True,null=True)
    gender    = models.CharField(max_length=100,blank=True,null=True)
    state    = models.CharField(max_length=100,blank=True,null=True)
    city    = models.CharField(max_length=100,blank=True,null=True)

    date_of_birth = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=30, blank=True,null=True,unique=True)
    balance = models.IntegerField(default=0, blank=True,null=True)
    deposite_balance = models.IntegerField(default=0, blank=True,null=True)
    total_amount_invested = models.IntegerField(default=0, blank=True,null=True)
    total_investement_count = models.IntegerField(default=0, blank=True,null=True)
    withdraw_total = models.IntegerField(default=0, blank=True,null=True) 
    is_email_verifield = models.BooleanField(default=False)
    bonus = models.IntegerField(default=0,blank=True,null=True)
    refferal = models.IntegerField(default=0,blank=True,null=True)
    recom_user_bonus = models.IntegerField(default=0,blank=True,null=True)



    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username']



    def __str__(self):
        return self.email

    def strname(self):
        return f"{self.username} "





class Referral(models.Model):
    user = models.OneToOneField(Account, on_delete = models.CASCADE)
    recommended_by = models.ForeignKey(Account,related_name='recom_user', on_delete=models.CASCADE,null=True, blank=True)
    recomended_users = models.ManyToManyField(Account, related_name='my_referrals',blank=True)
    date = models.DateTimeField(auto_now_add=True)




    def __str__(self):
        return self.user.username

    def strname(self):
        return f"{self.user.username} "