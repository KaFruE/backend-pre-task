from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.pagination import PageNumberPagination

from .models import AddressBook, Label
from .serializers import AddressBookSerializer, AddressBookInputSerializer


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

        serializer = AddressBookSerializer(address, many=True)

        return Response(serializer.data)


class AddressBookDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # serializer_class = AddressBookSerializer

    def get(self, request):
        return Response

    def post(self, request):
        serializer = AddressBookInputSerializer(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        return Response(data, status=HTTP_200_OK)


