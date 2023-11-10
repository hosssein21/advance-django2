from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from ...models  import Post
from .serializes import PostSerializer

@api_view()
def api_index(request):
    return Response({"detail":"This is Test Index view"})

@api_view(["GET","PUT","DELETE"])
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