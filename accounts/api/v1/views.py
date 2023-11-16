from rest_framework.response import Response 
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import (RegistrationSerializer,CustomAuthTokenSerializer,ChangePasswordSerializer,\
                            ProfileSerializer)
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash
from ...models import Profile
from django.shortcuts import get_object_or_404


class RegistrationApiView(GenericAPIView):
    
    serializer_class=RegistrationSerializer
    
    def post(self, request, *args, **kwargs):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data={
                'email':serializer.validated_data['email']
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    

class CustomObtainAuthToken(ObtainAuthToken):
    
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        

class CustomDiscardToken(APIView):
    
    permission_classes  =[IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='GET':
        return Response({'detail':'Change it'})
    
class ProfileApiView(RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
    def get_object(self):
        queryset=self.get_queryset()
        obj=get_object_or_404(queryset,user=self.request.user)
        return obj