from rest_framework import serializers
from .models import Solicitation

class SolicitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitation
        fields = '__all__'  # Inclui todos os campos do modelo
 
