import pandas as pd
from .models import Solicitation


file_path = "D:/dataVisualizationPython/Painel_Movimentacao_Maquinas.xlsx"




def import_survey_data(file_path):
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        Solicitation.objects.update_or_create(
            object_id=row['objectid'],
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
                'rescheduling': row['reprogramacao'],
                'cancellation': row['cancelamento'],
                'equipment_id': row['id_equip'],
                'reservation_date': row['data_reserva'],
                'calc_date': row['data_calc'],
                'reservation_time': row['hora_reserva'],
                'calc_time': row['hora_calc'],
                'origin_farm': row['fazenda_origem'],
                'destination_farm': row['fazenda_destino'],
                'center_1': row['centro_1'],
                'observation': row['observ'],
                'reservation_id': row['id_reserva'],
                'created_date': row['created_date'],
                'last_edited_date': row['last_edited_date'],
                'x_coordinate': row['x'],
                'y_coordinate': row['y'],
            }
        )
 
