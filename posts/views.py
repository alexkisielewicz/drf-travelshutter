from rest_framework import status, generics, permissions, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
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
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'category',
    ]
    
    def create(self, request, *args, **kwargs):
        """
        Create a post with the assigned post owner as 
        the user instance, along with tags as string.
        Tags are formatted to be unique, lowercase words,
        separated with commas.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Retrieve tags data from the request
        tags = request.data.get("tags", "")  
        # Split the tags string into individual lowercase tags separated with ","
        tag_list = [tag.strip().lower() for tag in tags.split(",") if tag.strip()]
        tag_str = ", ".join(tag_list)
        unique_tag_str = ", ".join(set(tag_list))
        # Save the post with assigned owner as user instance and tag string
        post = serializer.save(owner=self.request.user, tags=unique_tag_str)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    

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
