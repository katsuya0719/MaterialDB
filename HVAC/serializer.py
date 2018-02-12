from rest_framework import serializers
from .models import Chiller,CapacityFunction,EIRofTemp,EIRofPLR

class CapSerializer(serializers.ModelSerializer):
    class Meta:
        model=CapacityFunction
        exclude = ('chiller','name')

class EIRTSerializer(serializers.ModelSerializer):
    class Meta:
        model=EIRofTemp
        exclude = ('chiller', 'name')

class PLRSerializer(serializers.ModelSerializer):
    class Meta:
        model=EIRofPLR
        exclude = ('chiller', 'name')

class ChillerSerializer(serializers.ModelSerializer):
    cap=CapSerializer(read_only=True)
    eirtemp=EIRTSerializer(read_only=True)
    eirplr = PLRSerializer(read_only=True)

    class Meta:
        model=Chiller
        fields=('capacity','cop','chwtemp','conwtemp','cap','eirtemp','eirplr')
