from django.urls import path

from  .import views

urlpatterns = [
     path('sadmin/', views.index, name='sadmin'),
     path('sadmin/<str:app_name>/<str:mod>/', views.list_, name='sadmin-list'),
      path('sadmin/<str:app_name>/<str:mod>/add/', views.add_model, name='sadmin-add'),
     path('sadmin/<str:app_name>/referral/<int:pk>/change/', views.edit_ref, name='sadmin-edit_ref'),
     path('sadmin/<str:app_name>/account/<int:pk>/change/', views.edit_account, name='sadmin-edit_acc'),
     path('sadmin/<str:app_name>/investments/<int:pk>/change/', views.edit_investments, name='sadmin-edit-investments'),
     path('sadmin/<str:app_name>/packages/<int:pk>/change/', views.edit_packages, name='sadmin-edit-packages'),
     path('sadmin/<str:app_name>/transactions/<int:pk>/change/', views.edit_transactions, name='sadmin-edit-transactions'),
     path('sadmin/<str:app_name>/notification/<int:pk>/change/', views.edit_notification, name='sadmin-edit-notification'),

    ]