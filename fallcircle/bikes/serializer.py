from rest_framework import serializers
from .models import Wheel, Tyre, Chain, Groupset, Bike, ROTOR_CHOICES, CRANKSET_CHOICES

class Wheelserializer(serializers.ModelSerializer):
    class Meta:
        model = Wheel
        fields = '__all__'

class Tyreserializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = '__all__'

class Chainserializer(serializers.ModelSerializer):
     class Meta:
        model = Groupset
        fields = '__all__'

class Groupsetserializer(serializers.ModelSerializer):
    class Meta:
        model = Tyre
        fields = '__all__'

class Bikeserializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = '__all__'