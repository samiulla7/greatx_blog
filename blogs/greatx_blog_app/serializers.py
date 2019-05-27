from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Registration

class RegistrationSerializer(DocumentSerializer):
    class Meta:
        model = Registration
        fields = '__all__'