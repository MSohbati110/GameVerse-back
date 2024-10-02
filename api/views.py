from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class Register(APIView):
  def post(self, request):
    if User.objects.filter(username=request.data['username']).count() == 0:
      user = User.objects.create_user(request.data['username'], '', request.data['password'])
      refresh = RefreshToken.for_user(user)
      return Response(str(refresh.access_token))
    else:
      return Response('', status=400)