from django.shortcuts import render
from .serializers import UserSerializer, StationSerializer, SlotsSerializer
from .models import Station, StationAvailableSlots, User
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.decorators import api_view
from datetime import date
# class based seri to 
class userRequest(APIView):

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("User Created Successfully.", safe=False)
        return JsonResponse("User Registration Failed!", safe=False)

    # def get(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     print(pk)
    #     if pk:
    #         try:
    #             stationData = User.objects.get(email=pk)
    #             print("Station DAta -->", stationData)
    #             serializer = UserSerializer(stationData)
    #             return JsonResponse( serializer.data, safe=False)
    #         except User.DoesNotExist:
    #             raise Http404
    #     else:
    #         snippets = User.objects.all()
    #         serializer = UserSerializer(snippets, many=True)
    #         return JsonResponse(serializer.data, safe=False)
    



class stationRequest(APIView):

    def post(self, request):
        data = request.data
        serializer = StationSerializer(data = data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Your Charging Station is registered successfully", safe=False)
        return JsonResponse("Some went wrong, please try again", safe=False)


    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            try:
                stationData = Station.objects.get(stationid=pk)
                serializer = StationSerializer(stationData)
                return Response( serializer.data)
            except Station.DoesNotExist:
                raise Http404
        else:
            snippets = Station.objects.all()
            serializer = StationSerializer(snippets, many=True)
            return Response(serializer.data)


@api_view(['GET'])
def slotBooking(request , pk , mydate=date.today()):
    print(pk)
    print(mydate)
    if request.method == 'GET':
        print('1.......')
        data = StationAvailableSlots.objects.filter(stationid=pk)
        print("2..........")
        serializer = SlotsSerializer(data, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def slotBookingPost(request):
    if request.method == 'POST':
        print('132.......')
        data = request.data
        serializer = SlotsSerializer(data = data)
        print("188.......")
        if serializer.is_valid():
            print("388.....")
            serializer.save()
            return JsonResponse("Your slot is booked (method called [POST])", safe=False)
        return JsonResponse("Some went wrong, please try again[Post]", safe=False)

@api_view(['PATCH'])
def slotBookingPatch(request,pk):
    print("389.......")
    if request.method == 'PATCH':
            try:	
                # stationid = pk
                print("38idjid....")
                if StationAvailableSlots.objects.filter(stationid=pk):
                    print('inlsi888....')
                    id_inbody = request.data.get('stationid')
                    if pk != id_inbody:
                        device = StationAvailableSlots.objects.get(stationid=pk)
                        serializer = SlotsSerializer(device,data=request.data)
                        if serializer.is_valid():
                            serializer.save()
                            return JsonResponse("Your slot is booked(method called [PATCH]", safe=False)
                        return Response(serializer.errors)
                    else:
                        return JsonResponse("You cannot change station id", safe=False)
                return Response(serializer.errors)
            except Exception as e :
                    return JsonResponse("Some went wrong, please try again", safe=False)

