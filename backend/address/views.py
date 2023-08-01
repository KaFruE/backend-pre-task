from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework.pagination import PageNumberPagination

from .models import AddressBook, Label
from .pagination import CustomResultsSetPagination
from .serializers import AddressBookSerializer, AddressBookInputSerializer, AddressBookDetailSerializer


class AddressBookView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    # pagination_class = CustomResultsSetPagination
    serializer_class = AddressBookSerializer
    ordering_fields = ['name', 'email', 'phone', '-name', '-email', '-phone']

    """
    API 예시
    GET localhost:8000/api/address/view/
    Default 호출 (기본 출력)
    
    GET localhost:8000/api/address/view/?ordering=-phone
    정렬 가능 값 : 'name', 'email', 'phone', '-name', '-email', '-phone'
    """
    def get(self, request):
        # 정렬 적용
        order_param = self.request.query_params.get('ordering', None)
        ordering = order_param if order_param in self.ordering_fields else 'id'

        address = (AddressBook.objects.filter(user=self.request.user)) \
            .prefetch_related('labels').order_by(ordering)

        serializer = AddressBookSerializer(address, many=True)

        return Response(serializer.data, status=HTTP_200_OK)


class AddressBookDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """
    API 예시
    GET localhost:8000/api/address/detail/21/
    """
    def get(self, request, *args, **kwargs):
        address = get_object_or_404(AddressBook, pk=kwargs['pk'])
        serializer = AddressBookDetailSerializer(address)

        return Response(serializer.data, status=HTTP_200_OK)

    """
        API 예시
        POST localhost:8000/api/address/detail/
        {
            "profile" : "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
            "name" : "홍길동",
            "email" : "sr6442@naver.com",
            "phone" : "010-4560-6442",
            "company" : "가나다",
            "position" : "주임",
            "memo" : "메모",
            "address" : "서울시 노원구",
            "birthday" : "1995-03-06",
            "website" : "https://www.google.com",
            "labels" : [2],
            "new_labels" : ["보드게임 동아리"]
        }
    """
    def post(self, request):
        serializer = AddressBookInputSerializer(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        return Response(data, status=HTTP_200_OK)


