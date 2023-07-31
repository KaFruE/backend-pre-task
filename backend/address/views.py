from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.pagination import PageNumberPagination

from .models import AddressBook, Label
from .serializers import AddressBookSerializer

class AddressBookView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # pagination_class =
    serializer_class = AddressBookSerializer
    ordering_fileds = ['name', 'email', 'phone']

    # 정렬 적용
    # ordering = self.request.query_params.get('ordering', None)
    # if ordering in self.ordering_fields:
    #     queryset = queryset.order_by(ordering)