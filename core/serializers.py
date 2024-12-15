from rest_framework import serializers
from .models import Solicitation

class SolicitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitation
        fields = '__all__'  # Inclui todos os campos do modelo
 
from rest_framework import serializers
from .models import CM, Pranchas, Tritrem

class CMSerializer(serializers.ModelSerializer):
    class Meta:
        model = CM
        fields = '__all__'


class PranchasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pranchas
        fields = '__all__'


class TritremSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tritrem
        fields = '__all__'


from rest_framework import serializers
from .models import EscalaDia, EscalaNoite

class EscalaDiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscalaDia
        fields = '__all__'


class EscalaNoiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscalaNoite
        fields = '__all__'

