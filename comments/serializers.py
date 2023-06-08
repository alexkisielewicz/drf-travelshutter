from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    A class for a CommentSerializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id',
            'owner',
            'is_owner',
            'post',
            'created_at',
            'updated_at',
            'content',
            'profile_id',
            'profile_image',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Comment Detail Serializer class inherits from Comment Serializer
    """
    post = serializers.ReadOnlyField(source='post.id')