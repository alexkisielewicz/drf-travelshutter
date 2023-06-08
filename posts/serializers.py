from rest_framework import serializers
from .models import Post
from likes.models import Like
from tags.models import Tag
from tags.serializers import TagSerializer


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="profile.profile.image.url")
    comments_count = serializers.ReadOnlyField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    tags = serializers.CharField(max_length=200, required=False)
    
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
             "Image size is larger than 2 MB!"   
            )
        if value.image.width > 2500:
            raise serializers.ValidationError(
             "Image width is larger than 2048px!"   
            )
        if value.image.height > 2500:
            raise serializers.ValidationError(
             "Image height is larger than 2048px!"   
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