from rest_framework import serializers
from .models import Post
from likes.models import Like
from .constants import POST_CATEGORIES

class PostSerializer(serializers.ModelSerializer):
    """
    A class for Post serializer. 
    Validation of uploading image is applied
    to make sure file doesn't exceed 2MB size,
    or 2500px width and height. 
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    comments_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    tags = serializers.CharField()
    
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
             "Image size is larger than 2 MB!"   
            )
        if value.image.width > 2500:
            raise serializers.ValidationError(
             "Image width is larger than 2500px!"   
            )
        if value.image.height > 2500:
            raise serializers.ValidationError(
             "Image height is larger than 2500px!"   
            )    
        return value
        
    def get_is_owner(self, obj):
        # check post ownership
        request = self.context["request"]
        return request.user == obj.owner
    
    def get_like_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None 
    
    class Meta:
        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "category",
            "tags",
            "exif",
            "body",
            "image",
            'like_id',
            'comments_count',
            'likes_count',
        ]
        
class CategorySerializer(serializers.Serializer):
    categories = serializers.SerializerMethodField()

    def get_categories(self, obj):
        return [category[1] for category in POST_CATEGORIES]

    class Meta:
        fields = ['categories']