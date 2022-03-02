from rest_framework import status
from ApiCRUDapp.models import PostModel
from .serializers import PostSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
# from rest_framework.response import Response


class MyPostListAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    # def list(self, request):
    #     queryset = self.get_queryset()
    #     serializer = PostSerializer(queryset, many=True)
    #     return Response(serializer.data)


class MyPostDetailsAPI(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer


class PostCreateAPI(generics.CreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        serializer.save()

# class PostsView(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def get(self, request):
#         userObj = PostModel.objects.all()
#         serialized_obj = PostSerializer(userObj, many=True)
#         return Response(serialized_obj.data)

#     def post(self, request):
#         serialized_obj = PostSerializer(data= request.data)
#         if serialized_obj.is_valid():
#             serialized_obj.save()
#             return Response(serialized_obj.data, status=status.HTTP_201_CREATED)
#         return Response(serialized_obj.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreatePost(APIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     def get_object(self, pk):
#         serialized_obj = PostModel.objects.get(pk=pk)
#         try:
#             return PostModel.objects.get(pk=pk)
#         except PostModel.DoesNotExist:
#             return Response(serialized_obj.errors, status=status.HTTP_404_NOT_FOUND)
    
#     def get(self, request, pk):
#         user_obj = self.get_object(pk)
#         serialized_obj = PostSerializer(user_obj)
#         return Response(serialized_obj.data)
    
#     def put(self, request, pk):
#         user_obj=self.get_object(pk)
#         serialized_obj = PostSerializer(user_obj, data=request.data)
#         if serialized_obj.is_valid():
#             serialized_obj.save()
#             return Response(serialized_obj.data, status=status.HTTP_200_OK)
#         return Response(serialized_obj.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         user_obj = self.get_object(pk)
#         user_obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




