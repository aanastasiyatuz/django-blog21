from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField()
    class Meta:
        model = User
        fields = '__all__'
    
    def validate(self, attrs):
        p1 = attrs.get("password")
        p2 = attrs.pop("password_confirm")
        if p1 != p2:
            raise serializers.ValidationError("Passwords do not match")
        return attrs