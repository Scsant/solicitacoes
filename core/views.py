from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Solicitation
from .serializers import SolicitationSerializer
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import Solicitation
from django.db import transaction 

class SolicitationViewSet(ModelViewSet):
    queryset = Solicitation.objects.all()  # Retorna todas as solicitações
    serializer_class = SolicitationSerializer  # Usa o serializer que criamos


def home(request):
    return HttpResponse("<h1>Bem-vindo ao sistema de solicitações</h1>")

class ImportExcelView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # Permite envio de arquivos
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')  # Obtém o arquivo enviado
        if not file:
            return Response({'error': 'Nenhum arquivo enviado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Lê o arquivo Excel
            df = pd.read_excel(file)

            # Itera pelas linhas e salva no banco
            for _, row in df.iterrows():
                # Tratamento para valores inválidos em 'axles'
                axles_value = row['eixos']
                if not isinstance(axles_value, (int, float)) or pd.isna(axles_value):
                    # Define um valor padrão ou ignora o registro
                    axles_value = 0  # Você pode usar `None` se o campo no modelo permitir

                Solicitation.objects.update_or_create(
                    object_id=row['objectid'],  # Substitua pelos nomes das colunas do seu Excel
                    defaults={
                        'global_id': row['globalid'],
                        'menu': row['menu'],
                        'date': row['data_'] if pd.notna(row['data_']) else None,
                        'responsible_collaborator': row['colaborador_responsavel'],
                        'equipment': row['equipamento'],
                        'equipment_quantity': row['qnt_equipamento'] if pd.notna(row['qnt_equipamento']) else 0,
                        'cc_module': row['cc_modulo'],
                        'quantity': row['quantidade'] if pd.notna(row['quantidade']) else 0,
                        'axles': axles_value,  # Campo ajustado
                        'request': row['solicitacao'],
                        
                        'cancellation': row['cancelamento'] if pd.notna(row['cancelamento']) else None,
                        'equipment_id': row['id_equip'] if pd.notna(row['id_equip']) else None,
                        'reservation_date': row['data_reserva'] if pd.notna(row['data_reserva']) else None,
                        'calc_date': row['data_calc'] if pd.notna(row['data_calc']) else None,
                        'reservation_time': row['hora_reserva'] if pd.notna(row['hora_reserva']) else None,
                        'calc_time': row['hora_calc'] if pd.notna(row['hora_calc']) else None,
                        'origin_farm': row['fazenda_origem'],
                        'destination_farm': row['fazenda_destino'],
                        'center_1': row['centro_1'] if pd.notna(row['centro_1']) else None,
                        'observation': row['observ'] if pd.notna(row['observ']) else None,
                        'reservation_id': row['id_reserva'],
                        'created_date': row['created_date'] if pd.notna(row['created_date']) else None,
                        'last_edited_date': row['last_edited_date'] if pd.notna(row['last_edited_date']) else None,
                        'x_coordinate': row['x'] if pd.notna(row['x']) else 0,
                        'y_coordinate': row['y'] if pd.notna(row['y']) else 0,
                    }
                )
            return Response({'message': 'Dados importados com sucesso'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
