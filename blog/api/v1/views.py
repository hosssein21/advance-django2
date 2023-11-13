from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,action
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from ...models  import Post,Category
from .serializes import PostSerializer,CategorySerializer

@api_view()
def api_index(request):
    return Response({"detail":"This is Test Index view"})

@api_view(["GET","PUT","DELETE"])
@permission_classes([IsAuthenticated])
def post_detail(request,pk):
    if request.method=="GET":
        try:
            post=Post.objects.get(pk=pk,Active=1)
            serializer=PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({"detail":"This is not found"},status=status.HTTP_404_NOT_FOUND)

    elif request.method=="PUT":
        post=get_object_or_404(Post,pk=pk,Active=1)
        serializer=PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    elif request.method=="DELETE":
        post=get_object_or_404(Post,pk=pk,Active=1)
        post.delete()
        return Response({"detail":"item deleted successfully"})
    
    
        
@api_view(['GET', 'POST'])
def all_post(request):
    if request.method=='GET':
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
class PostList(APIView):
    
    def get(self, request):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class PostDetail(APIView):
    
    permission_classes=[IsAuthenticated]
    serializer_class=PostSerializer
    
    def get(self, request,pk):
        
        try:
            post=Post.objects.get(pk=pk,Active=1)
            serializer=self.serializer_class(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response({"detail":"This is not found"},status=status.HTTP_404_NOT_FOUND)
        
        
    def put(self, request,pk):
        
        post=get_object_or_404(Post,pk=pk,Active=1)
        serializer=PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request,pk):
        post=get_object_or_404(Post,pk=pk,Active=1)
        post.delete()
        return Response({"detail":"item deleted successfully"})
        
        
class PostListGeneric(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = PostSerializer
    queryset=Post.objects.all()
    
class PostDetailGeneric(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = PostSerializer
    queryset=Post.objects.filter(Active=1)
    

class PostViewSet(viewsets.ViewSet):
    
    permission_classes=[IsAuthenticated]
    serializer_class = PostSerializer
    queryset=Post.objects.filter(Active=1)
    
    def list(self, request):
        serializer=self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request,pk=None):
        post_object=get_object_or_404(self.queryset,pk=pk)
        serializer=self.serializer_class(post_object)
        return Response(serializer.data)
    
class PostModelViewSet(viewsets.ModelViewSet):
     
    permission_classes=[IsAuthenticated]
    serializer_class = PostSerializer
    queryset=Post.objects.filter(Active=1)
    
    @action(methods=['get'],detail=False)
    def get_ok(self,request):
        return Response({'detail':"This is Ok"})
    

class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated]
    serializer_class = CategorySerializer
    queryset=Category.objects.all()