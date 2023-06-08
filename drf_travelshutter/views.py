from rest_framework.views import APIView
from rest_framework.response import Response

class RootView(APIView):
    def get(self, request):
        data = {
            'message': 'Welcome to TravelShutter API!',
            'endpoints': {
                'profiles': '/profiles',
                'posts': '/posts',
                'comments': '/comments',
                'likes': '/likes',
                'followers': '/followers',
            }
        }
        return Response(data)