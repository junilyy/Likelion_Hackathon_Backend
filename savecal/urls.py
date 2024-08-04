from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('food/', FoodCreateView.as_view(), name='food-create'),
    path('exercise/', ExerciseCreateView.as_view(), name='exercise-create'),
    path('food/list/', FoodListView.as_view(), name='food-list'),
    path('exercise/list/', ExerciseListView.as_view(), name='exercise-list'),
    path('user/profile/', UserProfileView.as_view(), name='user-profile'),
    path('total-calories/', TotalCaloriesView.as_view(), name='total-calories'),
    path('user/bmi/', UserBMIView.as_view(), name='user-bmi'),
    # 모든 기능을 처리하는 단일 엔드포인트
    path('combined/<str:view_type>/', CombinedView.as_view(), name='combined-view'),
]

