from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home, name='home'),
    path('add/',add_account,name='add'),
    path('view/', View_account, name='view_ac'),
    path('edit_account/<int:id>',edit_account,name='edit_account'),
    path('delete_account/<int:id>',delete_account,name='delete_account'),
    path('Transfer/', transfer, name='Transfer'),
    path('View_Transfer/', view_transfer, name='View_Transfer'),
]