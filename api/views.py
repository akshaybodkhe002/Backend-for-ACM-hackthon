from django.shortcuts import render
from .serializers import UserSerializer, StationSerializer, SlotsSerializer
from .models import Station, StationAvailableSlots, User
from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response
from django.http import Http404
from rest_framework.decorators import api_view
from datetime import date
from rest_framework.parsers import JSONParser
import io
import json
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

# To display avaliable slots to user
@api_view(['GET'])
def slotBooking(request , pk , mydate=str(date.today())):
    print(pk)
    print(mydate)
    if request.method == 'GET':
        print('1.......')
        d = StationAvailableSlots.objects.filter(stationid=pk,date=mydate)
        print(d)
        if bool(d):
            print("2..........")
            serializer = SlotsSerializer(d, many=True)
            print("3.......")
            return Response(serializer.data)
        else:
            print("ele.....")
            # en = StationAvailableSlots(stationid = pk, date = mydate ).save()
            # serializer = SlotsSerializer(en, many=True)
            return Response({'msg':'All slots are availabe!'} )

@api_view(['POST'])
def slotBookingPost(request):
    if request.method == 'POST':
        print('132.......')
        # data = request.data
        data = JSONParser().parse(request)
        print(data)
        serializer = SlotsSerializer(data = data,partial=True)
        print(serializer)
                  
        print("188.......")
        if serializer.is_valid():
            print("388.....")
            serializer.save()
            return JsonResponse("Your slot is booked (method called [POST])", safe=False)
        else:
            serialized_data = serializer.data
            print("Else.....")
            print(serialized_data['stationid'])
            id = serialized_data['stationid']
            dt = serialized_data['date']
            s1 = serialized_data['slot1']
            s2 = serialized_data['slot2']
            s3 = serialized_data['slot3']
            s4 = serialized_data['slot4']
            s5 = serialized_data['slot5']
            s6 = serialized_data['slot6']
            s7 = serialized_data['slot7']
            s8 = serialized_data['slot8']
            s9 = serialized_data['slot9']
            s10 = serialized_data['slot10']
            s11 = serialized_data['slot11']
            s12 = serialized_data['slot12']
            if StationAvailableSlots.objects.filter(stationid=id,date = dt).exists():
                print("13.....")
                StationAvailableSlots.objects.filter(stationid=id, date = dt).update(slot1=s1,slot2=s2,slot3=s3,slot4=s4,slot5=s5,slot6=s6,slot7=s7,slot8=s8,slot9=s9,slot10=s10,slot11=s11,slot12=s12);
                return JsonResponse("Your slot is booked.[Update method]", safe=False)
            else:
                print("838.....")
                StationAvailableSlots.objects(stationid_id=id, date = dt,slot1=s1,slot2=s2,slot3=s3,slot4=s4,slot5=s5,slot6=s6,slot7=s7,slot8=s8,slot9=s9,slot10=s10,slot11=s11,slot12=s12).save()
                return JsonResponse("Your slot is booked.[Update method]", safe=False)

    return JsonResponse("Some went wrong, please try again[Post]", safe=False)



