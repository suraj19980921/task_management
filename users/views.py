from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from .serializers import UserSerializer, LoginSerializer

class UserViewSet(viewsets.GenericViewSet):
    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({'success_message': 'User Sucessfully Created.','user_id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        print("control received")
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user_id': user.id}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        try:
            token = request.headers.get('Authorization').split()[1]
            Token.objects.filter(key=token).delete()
            return Response({'success': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except:
            return Response({'error': 'Invalid token or authorization header.'}, status=status.HTTP_400_BAD_REQUEST)
