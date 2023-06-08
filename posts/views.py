from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer
from drf_travelshutter.permissions import IsOwnerOrReadOnly
from django.db.models import Count


class PostList(generics.ListCreateAPIView):
    # render create post form
    serializer_class = PostSerializer
    # user has to be logged in in order to create posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count(
            'comment',
            distinct=True
        ),
        likes_count=Count(
            'likes',
            distinct=True
        )
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        # filters.SearchFilter,
        # DjangoFilterBackend,
    ]
    ordering_fields = [
        'comments_number',
        'likes_number',
        'likes__created_at',
    ]
    
    def create_post(self, serializer):
        # method to assign owner to the post before save
        serializer.save(owner=self.request.user)
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # check if requesting user is post owner
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(
        comments_count=Count(
            'comment',
            distinct=True
        ),
        likes_count=Count(
            'likes',
            distinct=True
        )
    ).order_by('-created_at')
