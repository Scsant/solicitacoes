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

class SolicitationViewSet(ModelViewSet):
    queryset = Solicitation.objects.all()  # Retorna todas as solicitações
    serializer_class = SolicitationSerializer  # Usa o serializer que criamos


def home(request):
    return HttpResponse("<h1>Bem-vindo ao sistema de solicitações</h1>")


class ImportExcelView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # Para permitir upload de arquivos

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')  # Pega o arquivo enviado no request
        if not file:
            return Response({'error': 'Nenhum arquivo enviado'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Lê o arquivo Excel
            df = pd.read_excel(file)
            # Itera pelas linhas e salva no banco
            for _, row in df.iterrows():
                Solicitation.objects.update_or_create(
                    object_id=row['objectid'],  # Substitua pelos nomes das colunas do seu Excel
                    defaults={
                        'global_id': row['globalid'],
                        'menu': row['menu'],
                        'date': row['data_'],
                        'responsible_collaborator': row['colaborador_responsavel'],
                        'equipment': row['equipamento'],
                        'equipment_quantity': row['qnt_equipamento'],
                        'cc_module': row['cc_modulo'],
                        'quantity': row['quantidade'],
                        'axles': row['eixos'],
                        'request': row['solicitacao'],
                        'rescheduling': row.get('reprogramacao'),  # Valores opcionais
                        'cancellation': row.get('cancelamento'),
                        'equipment_id': row.get('id_equip'),
                        'reservation_date': row['data_reserva'],
                        'calc_date': row['data_calc'],
                        'reservation_time': row['hora_reserva'],
                        'calc_time': row['hora_calc'],
                        'origin_farm': row['fazenda_origem'],
                        'destination_farm': row['fazenda_destino'],
                        'center_1': row.get('centro_1'),
                        'observation': row.get('observ'),
                        'reservation_id': row['id_reserva'],
                        'created_date': row['created_date'],
                        'last_edited_date': row['last_edited_date'],
                        'x_coordinate': row['x'],
                        'y_coordinate': row['y'],
                    }
                )
            return Response({'message': 'Dados importados com sucesso'}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
