from rest_framework import serializers
from ...models import Post,Category

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields=['id','name']

class PostSerializer(serializers.ModelSerializer):
    #content=serializers.ReadOnlyField()
    snippet=serializers.ReadOnlyField(source='get_snippet')
    relative_url=serializers.URLField(source='get_absolute_api_url',read_only=True)
    absolute_url=serializers.SerializerMethodField()
    
    class Meta:
        model=Post
        fields=["title","content","author","category",'snippet','relative_url','absolute_url']
        
    def get_absolute_url(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)