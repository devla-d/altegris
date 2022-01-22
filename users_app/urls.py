from django.urls import path


from . import views

urlpatterns = [
    path('dashboard/', views.index, name="dashboard"),
    path('create-investment/', views.create_investment, name="create-investment"),
    path('wallet/', views.wallet, name="wallet"),
    path('history/', views.history, name="history"),
    path('withdraw-funds/', views.withdraw, name="withdraw"),
    path('deposit-funds/', views.deposit, name="deposit"),
    path('notification/', views.notification, name="notification"),
    path('settings/', views.settings, name="settings"),
    path('security/', views.security, name="security"),
    path('account/', views.account, name="account"),


     path('claim-investment/', views.claim_investment, name="claim-investment"),
    
   
]
