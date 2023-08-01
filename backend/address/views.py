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
    ordering_fields = ['name', 'email', 'phone', '-name', '-email', '-phone']

    def get(self, request):
        # 정렬 적용
        order_param = self.request.query_params.get('ordering', None)
        ordering = order_param if order_param in self.ordering_fields else 'id'

        address = (AddressBook.objects.filter(user=self.request.user)) \
            .prefetch_related('labels').order_by(ordering)

        serializers = AddressBookSerializer(address, many=True)

        return Response(serializers.data)


class AddressBookInputView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
