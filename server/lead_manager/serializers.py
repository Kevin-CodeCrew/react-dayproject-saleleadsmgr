from rest_framework import serializers
from .models import UserModel, SalesLeadModel, CompanyModel

# Serializer for our user model
class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

# Serializer for our company model
class CompanyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'


# Serializer for our sales lead model
# Note that it incorporates the linked User and Company instance
class SalesLeadModelSerializer(serializers.ModelSerializer):
    companyFk = CompanyModelSerializer(many=False)
    userFk = UserModelSerializer(many=False)

    class Meta:
        model = SalesLeadModel
        fields = [
            'name',
            'email',
            'message',
            'created_at',
            'companyFk',
            'userFk'
        ]
