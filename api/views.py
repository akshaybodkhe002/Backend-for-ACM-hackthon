# from django.shortcuts import render
# from .serializers import UserSerializer, StationSerializer, SlotsSerializer
# from rest_framework.views import APIView
# from django.http.response import JsonResponse
# from rest_framework.response import Response

# # class based seri to 
# class userRequest(APIView):

#     def post(self, request):
#         data = request.data
#         serializer = UserSerializer(data = data)

#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse("User Created Successfully.", safe=False)
#         return JsonResponse("User Registration Failed!", safe=False)



