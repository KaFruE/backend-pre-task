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


class AddressBookInputSerializer(serializers.ModelSerializer):
    new_labels = serializers.ListField(default=[], child=serializers.CharField(required=False), allow_empty=True)
    labels = serializers.ListField(default=[], child=serializers.IntegerField(required=False), allow_empty=True)
    class Meta:
        model = AddressBook
        fields = ['profile', 'name', 'email', 'phone', 'company', 'position', 'memo', 'address', 'birthday', 'website', 'labels', 'new_labels']

    def validate(self, data):
        labels = list(data.get("labels"))
        new_labels = list(data.get('new_labels'))
        label_list = list()

        if labels:
            for label in labels:
                obj = Label.objects.filter(id=label, user=self.context['request'].user)

                if not obj:
                    msg = "Unable to register with provided id : " + label + " not available."
                    raise serializers.ValidationError(msg, code="incorrect")
                else:
                    label_list.append(label)

        if new_labels:
            for new_label in new_labels:
                objs = Label.objects.filter(name=new_label, user=self.context['request'].user)

                if objs:
                    msg = "Unable to register with provided name : " + new_label + " already exist."
                    raise serializers.ValidationError(msg, code="already exist")
                else:
                    new_label_obj = Label.objects.create(name=new_label, user=self.context['request'].user)
                    print(new_label_obj)
                    label_list.append(new_label_obj.id)


        m = AddressBook(
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
            labels=label_list
        )

        m.save()
        return m
