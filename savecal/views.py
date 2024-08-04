from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User  
from .serializers import UserSerializer 
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Food, Exercise
from .serializers import FoodSerializer, ExerciseSerializer
from django.db import models

class UserProfileView(APIView):  #user 정보 받아오는 예시.
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class TotalCaloriesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        food_calories = Food.objects.filter(user=user).aggregate(total_calories=models.Sum('calories'))['total_calories'] or 0
        exercise_calories = Exercise.objects.filter(user=user).aggregate(total_calories_burned=models.Sum('calories_burned'))['total_calories_burned'] or 0
        total_calories = {
            'total_food_calories': food_calories,
            'total_exercise_calories': exercise_calories,
        }
        return Response(total_calories)

class UserBMIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        height_in_meters = user.height / 100  # assuming height is stored in centimeters
        bmi = user.weight / (height_in_meters ** 2)
        bmi_data = {
            'height': user.height,
            'weight': user.weight,
            'bmi': bmi,
        }
        return Response(bmi_data)

class FoodCreateView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

class ExerciseCreateView(generics.CreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]
    
class FoodListView(generics.ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]

class ExerciseListView(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]
# part1
# 1. 음식과 운동 항목들, date, user 저장할 수 있는 model 구축(frontend에서 보내주는 값 DB에 저장해야 되니까.)
# 2. frontend에서 POST하는 음식-운동 칼로리, 날짜, 로그인한 유저 정보(username?)를 DB에 POST하는 view 구현.

# part2
# 1. 위 모델의 DB에 저장된 값 frontend로 GET하는 view 구현 (섭취 칼로리와 소모 칼로리 총량 반환)
# -> frontend에서 섭취 및 소모 칼로리를 넘겨준다는 가정하에 순서 짬. 만약에 숫자로 못 넘기고 boolean으로 넘어오면 음식, 운동별 칼로리를 따로 DB에 저장해 GET 해야함.

# part3
# 1. 로그인한 user 정보 불러오고 공식 이용해서 BMI 값 등 GET하는 view 구현.