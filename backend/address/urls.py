from django.urls import path

from .views import AddressBookView, AddressBookDetailView

app_name = 'address'

urlpatterns = [
    path('view/', AddressBookView.as_view(), name='address_view'),
    path('detail/', AddressBookDetailView.as_view(), name='address_detail')
]