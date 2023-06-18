from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    
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
        # check profile ownership
        request = self.context['request']
        return request.user == obj.owner
    
    def get_following_id(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, 
                followed=obj.owner
            ).first()
            return following.id if following else None
        return None
    
    class Meta:
        model = Profile
        fields = [
            "id",
            "owner",
            "name",
            "bio",
            "instagram",
            "equipment",
            "created_at",
            "updated_at",
            "content",
            "image",
            "is_owner",
            "following_id",
            "posts_count",
            "followers_count",
            "following_count",
        ]