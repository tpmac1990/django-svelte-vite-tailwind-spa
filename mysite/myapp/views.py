from rest_framework.views import APIView
from rest_framework.response import Response


class BlogsList(APIView):
    """  """
    def get(self, request):
        blogs = [
            {'id': 1, 'title': 'horses'},
            {'id': 2, 'title': 'cats'},
            {'id': 3, 'title': 'dogs'}
        ]
        return Response({'blogs': blogs})
    
class BlogIndex(APIView):
    """ """
    def get(self, request, pk):
        blogs = {
            1: {'title': 'horses', 'content': 'horses are the best'},
            2: {'title': 'cats', 'content': 'cats are the best'},
            3: {'title': 'dogs', 'content': 'dogs are the best'}
        }
        blog = blogs[pk]
        return Response({'blog': blog})