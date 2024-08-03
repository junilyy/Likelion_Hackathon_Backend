from rest_framework import serializers
from user.models import User  # 사용자 모델을 임포트

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'nickname', 'email', 'age', 'phonenumber', 'height', 'weight', 'gender', 'exercise_frequency', 'created_at', 'updated_at')
