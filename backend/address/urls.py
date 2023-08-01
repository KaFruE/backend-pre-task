from django.urls import path

from .views import AddressBookView

app_name = 'address'

urlpatterns = [
    path('view/', AddressBookView.as_view(), name='address_view'),
]