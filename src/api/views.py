from rest_framework.generics import ListAPIView
from blog.models import Post
from .serializers import PostSerializer



class UserPostListAPIView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        print('injaaaaaaaaaaaaaaa')
        return Post.objects.filter(user_id=user_id)

