from .models import AddressBook, Label
from rest_framework import serializers

class AddressBookSerializer(serializers.ModelSerializer):
    company_detail = serializers.SerializerMethodField('get_company_detail')
    labels = serializers.SlugRelatedField(many=True, queryset=Label.objects.all(), slug_field='name')

    class Meta:
        model = AddressBook
        fields = ['profile', 'name', 'email', 'phone', 'company_detail', 'labels']

    def get_company_detail(self, obj):
        company_detail = '%s %s' % (obj.company, obj.position)
        return company_detail.strip()