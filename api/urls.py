from django.urls import path , register_converter
from .views import userRequest, stationRequest, slotBooking, slotBookingPost
from .converter import DateConverter

register_converter(DateConverter, 'date')

urlpatterns = [
    path('register/', userRequest.as_view() ),
    # path('register/<string>', userRequest.as_view() ),  # To send user data to frontend
    path('stationRegister/', stationRequest.as_view()),
    path('stationRegister/<int:pk>/', stationRequest.as_view()),
    path('slotbooking/<int:pk>/', slotBooking),
    path('slotbooking/<int:pk>/<str:mydate>/', slotBooking),
    path('slotBookingPost/', slotBookingPost),
    # path('slotBookingPatch/<int:pk>', slotBookingPatch),
]