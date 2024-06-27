from django.shortcuts import render, get_object_or_404
from bikes.models import Bike, Wheel, Chain, Groupset, Tyre
from rest_framework.response import Response
from rest_framework.decorators import api_view
from.serializer import Wheelserializer, Tyreserializer, Chainserializer, Groupsetserializer, Bikeserializer
from rest_framework.views import APIView

class Wheel(APIView):
    def get(self, request):
        Wheels = Wheel #complex data
        serializer = Wheelserializer(Wheels, many=True)
        return Response(serializer.data)
    
# Create your views here.

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