from django.db import models
from core.models import TempModel
from accounts.models import User


class AddressBook(TempModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='사용자')
    profile = models.URLField(null= True, verbose_name='프로필 URL')
    name = models.CharField(max_length=50, verbose_name='이름')
    email = models.EmailField(verbose_name='이메일')
    phone = models.CharField(max_length=20, verbose_name='핸드폰 번호')
    company = models.CharField(null=True, max_length=20, verbose_name='회사')
    position = models.CharField(null=True, max_length=20, verbose_name='회사 직책')
    memo = models.CharField(null=True, max_length=150, verbose_name='메모')
    address = models.CharField(null=True, max_length=50, verbose_name='주소')
    birthday = models.DateField(null=True, auto_now=False, verbose_name='생년월일')
    website = models.URLField(null=True, verbose_name='사이트 URL')
    labels = models.ManyToManyField('Label', db_table="address_label")

    class Meta:
        db_table = "addressbook"

    def __str__(self):
        return self.name

class Label(TempModel):
    name = models.CharField(max_length=50, verbose_name='라벨 이름')

    class Meta:
        db_table = "label"

    def __str__(self):
        return self.name