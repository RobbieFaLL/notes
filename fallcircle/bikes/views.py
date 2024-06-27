from django.shortcuts import render, get_object_or_404
from .models import Bike, Wheel, Chain, Groupset, Tyre
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Wheelserializer, Tyreserializer, Chainserializer, Groupsetserializer, Bikeserializer
from rest_framework.views import APIView

class Wheeldataview(APIView):
    def get(self, request):
        wheels = Wheel.objects.all()
        serializer = Wheelserializer(wheels, many=True)
        return Response(serializer.data)
    
class Tyredataview(APIView):
    def get(self, request):
        Tyres = Tyre.objects.all()
        serializer = Tyreserializer(Tyres, many=True)
        return Response(serializer.data)
    
class Chaindataview(APIView):    
    def get(self, request):    
        Chains = Chain.objects.all()
        serializer = Chainserializer(Chains, many=True)
        return Response(serializer.data)
    
class Bikedataview(APIView):
    def get(self, request):
        Bikes = Bike.objects.all()
        serializer = Bikeserializer(Bikes, many=True)
        return Response(serializer.data)
    
class Groupsetdataview(APIView):
    def get(self, request):
        Groupsets = Groupset.objects.all()
        serializer = Groupsetserializer(Groupsets, many=True)
        return Response(serializer.data)


def bikes(request):
    bikes = Bike.objects.all()
    context = {'bikes':bikes}
    print(context)
    return render(request, 'bikes.html', context)

def bikes_content(request, id):
    #getting blog content from database if it exists
    bike = get_object_or_404(Bike, pk=id)
    #pass blog to context
    context = {
        'bike':bike, 
    }
    #pass request,template context to render
    return render(request, 'bikescontent.html', context)

def API_content(request):
    return render(request, 'bikesAPI.html')