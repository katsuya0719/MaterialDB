from rest_framework import serializers
from .models import Chiller,CapacityFunction,EIRofTemp,EIRofPLR

class CapSerializer(serializers.ModelSerializer):
    class Meta:
        model=CapacityFunction
        fields = ('c1','c2','c3')

class EIRTSerializer(serializers.ModelSerializer):
    class Meta:
        model=EIRofTemp
        fields = ('c1','c2','c3')

class PLRSerializer(serializers.ModelSerializer):
    class Meta:
        model=EIRofPLR
        fields = ('c1','c2','c3')

class ChillerSerializer(serializers.ModelSerializer):
    #cap=CapSerializer(read_only=True)
    #eirtemp=EIRTSerializer(read_only=True)
    #eirplr = PLRSerializer(read_only=True)
    cap = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model=Chiller
        fields=('capacity','cop','chwtemp','conwtemp','cap')
