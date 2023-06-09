from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from .serializers import PostSerializer
from drf_travelshutter.permissions import IsOwnerOrReadOnly
from django.db.models import Count


def format_tags(tags):
    """
    Function to format tags by removing duplicates,
    sorting alphabetically, and joining with commas.
    """
    tags = tags.lower().replace(',', ' ').split()
    unique_tags = sorted(set(tags))
    formatted_tags = ', '.join(unique_tags)
    return formatted_tags


class PostList(generics.ListCreateAPIView):
    # Render create post form
    serializer_class = PostSerializer
    # user has to be logged in in order to create posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count(
            "comment",
            distinct=True
        ),
        likes_count=Count(
            "likes",
            distinct=True
        )
    ).order_by("-created_at")
    
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    
    search_fields = [
        "owner__username",
        "title",
        "category",
    ]
        
    ordering_fields = [
        "comments_number",
        "likes_number",
        "likes__created_at",
    ]
    
    filterset_fields = [
        "owner__followed__owner__profile",
        "likes__owner__profile",
        "owner__profile",
        "category",
    ]
    
    def perform_create(self, serializer):
        """
        Method to save post instance with assigned
        user as owner and formatted tags.
        """
        tags = self.request.data.get('tags', '')
        formatted_tags = format_tags(tags)
        serializer.save(owner=self.request.user, tags=formatted_tags)
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # check if requesting user is post owner
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        comments_count=Count(
            "comment",
            distinct=True
        ),
        likes_count=Count(
            "likes",
            distinct=True
        )
    ).order_by("-created_at")
    
    def perform_update(self, serializer):
        """
        Method to update post instance with formatted tags.
        """
        tags = self.request.data.get('tags', '')
        formatted_tags = format_tags(tags)
        serializer.save(tags=formatted_tags)
