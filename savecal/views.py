from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User  
from .serializers import UserSerializer 
from rest_framework.permissions import IsAuthenticated

class UserProfileView(APIView):  #user 정보 받아오는 예시.
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

# part1
# 1. 음식과 운동 항목들, date, user 저장할 수 있는 model 구축(frontend에서 보내주는 값 DB에 저장해야 되니까.)
# 2. frontend에서 POST하는 음식-운동 칼로리, 날짜, 로그인한 유저 정보(username?)를 DB에 POST하는 view 구현.

# part2
# 1. 위 모델의 DB에 저장된 값 frontend로 GET하는 view 구현 (섭취 칼로리와 소모 칼로리 총량 반환)
# -> frontend에서 섭취 및 소모 칼로리를 넘겨준다는 가정하에 순서 짬. 만약에 숫자로 못 넘기고 boolean으로 넘어오면 음식, 운동별 칼로리를 따로 DB에 저장해 GET 해야함.

# part3
# 1. 로그인한 user 정보 불러오고 공식 이용해서 BMI 값 등 GET하는 view 구현.