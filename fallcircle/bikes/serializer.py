from rest_framework import serializers
from .models import Wheel, Tyre, Chain, Groupset, Bike

class Wheelserializer(serializers.ModelSerializer):
    class Meta:
        model = Wheel
        fields = '__all__'

class Chainserializer(serializers.ModelSerializer):
    class Meta:
        model = Chain
        fields = '__all__'

class Groupsetserializer(serializers.ModelSerializer):
    chain = Chainserializer()
    class Meta:
        model = Groupset
        fields = '__all__'

class Tyreserializer(serializers.ModelSerializer):
    class Meta:
        model = Tyre
        fields = '__all__'

class Bikeserializer(serializers.ModelSerializer):
    wheels = Wheelserializer()
    tyre = Tyreserializer()
    groupset = Groupsetserializer()
    class Meta:
        model = Bike
        fields = '__all__'