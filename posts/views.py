from django.http import Http404
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from drf_travelshutter.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    # render create post form
    serializer_class = PostSerializer
    # user has to be logged in in order to create posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    
    def create_post(self, serializer):
        # method to assign owner to the post before save
        serializer.save(owner=self.request.user)
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # check if requesting user is post owner
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
