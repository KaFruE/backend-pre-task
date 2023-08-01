from django.db import transaction

from .models import AddressBook, Label
from rest_framework import serializers
from django.forms.models import model_to_dict

class AddressBookSerializer(serializers.ModelSerializer):
    company_detail = serializers.SerializerMethodField('get_company_detail')
    labels = serializers.SlugRelatedField(many=True, queryset=Label.objects.all(), slug_field='name')

    class Meta:
        model = AddressBook
        fields = ['profile', 'name', 'email', 'phone', 'company_detail', 'labels']

    def get_company_detail(self, obj):
        company_detail = '%s %s' % (obj.company, obj.position)
        return company_detail.strip()


class AddressBookInputSerializer(serializers.ModelSerializer):
    new_labels = serializers.ListField(default=[], child=serializers.CharField(required=False), allow_empty=True)
    labels = serializers.ListField(default=[], child=serializers.IntegerField(required=False), allow_empty=True)

    class Meta:
        model = AddressBook
        fields = ['profile', 'name', 'email', 'phone', 'company', 'position', 'memo', 'address', 'birthday', 'website', 'labels', 'new_labels']

    @transaction.atomic(using='default')
    def validate(self, data):
        labels = list(data.get("labels"))  # 기존 존재 하는 라벨 ID 리스트
        new_labels = list(data.get('new_labels'))  # 새로 추가 하고자 하는 라벨 이름
        label_list = list()  # return 에 보낼 반영 완료된 label 리스트

        # 주소록 반영 이후 라벨 반영 부분에서 문제 시 라벨 부분이 반영 안되는 것을 해결 하기 위해 반영
        with transaction.atomic():
            address = AddressBook(
                profile=data.get("profile"),
                name=data.get("name"),
                email=data.get("email"),
                phone=data.get("phone"),
                company=data.get("company"),
                position=data.get("position"),
                memo=data.get("memo"),
                address=data.get("address"),
                birthday=data.get("birthday"),
                website=data.get("website"),
                user=self.context['request'].user
            )
            address.save()

            if labels:
                for label in labels:
                    obj = Label.objects.filter(id=label, user=self.context['request'].user)

                    if not obj:
                        msg = "Unable to register with provided id : " + label + " not available."
                        raise serializers.ValidationError(msg, code="incorrect")

                    address.labels.add(label)
                    label_list.append(obj[0].name)

            if new_labels:
                for new_label in new_labels:
                    objs = Label.objects.filter(name=new_label, user=self.context['request'].user)

                    if objs:
                        msg = "Unable to register with provided name : " + new_label + " already exist."
                        raise serializers.ValidationError(msg, code="already exist")

                    new_label_obj = Label.objects.create(name=new_label, user=self.context['request'].user)
                    address.labels.add(new_label_obj)
                    label_list.append(new_label)

        address_dict = model_to_dict(address)
        address_dict['labels'] = label_list

        return address_dict
