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

import pandas as pd
from .models import CM, Pranchas, Tritrem, EscalaDia, EscalaNoite

def import_internal_data(file_path):
    # Lê todas as abas da planilha
    sheets = pd.read_excel(file_path, sheet_name=None)
    if 'CM' in sheets:
        cm_df = sheets['CM']
        cm_df.columns = cm_df.columns.str.strip()  # Remove espaços extras dos nomes das colunas
        for _, row in cm_df.iterrows():
            CM.objects.update_or_create(
                quantidade=row['QUANTIDADE'],  # Nome correto da coluna
                btf=row['btf']  # Nome atualizado da coluna
            )

    if 'PRANCHAS' in sheets:
        pranchas_df = sheets['PRANCHAS']
        pranchas_df.columns = pranchas_df.columns.str.strip()  # Remove espaços extras

        # Verifique se a coluna 'FROTA' existe
        if 'FROTA' not in pranchas_df.columns:
            raise ValueError("Coluna 'FROTA' não encontrada na aba PRANCHAS")

        for _, row in pranchas_df.iterrows():
            Pranchas.objects.update_or_create(
                quan=row['QUAN/'],  # Verifique os nomes reais das colunas
                frota=row['FROTA'],  # Ajuste para o nome correto da coluna
                defaults={
                    'placa': row['PLACA'],
                    'fabricante': row['FABRICANTE'],
                    'tipo': row['TIPO'],
                    'especificacoes': row['ESPECIFICAÇÕES'],
                    'chassis': row['CHASSIS'],
                }
            )



    # Processa a aba TRITREM
    if 'TRITREM' in sheets:
        tritrem_df = sheets['TRITREM']
        for _, row in tritrem_df.iterrows():
            Tritrem.objects.update_or_create(
                btf_01=row['btf_01'],
                defaults={
                    'placa': row['PLACA'],
                    'primeira_carreta': row['1° Carreta'],
                    'segunda_carreta': row['2° Carreta'],
                    'terceira_carreta': row['3° Carreta'],
                    'fabricante_cm': row['FABRICANTE CM'],
                    'fabricante_conjunto': row['FABRICANTE CONJUNTO']
                }
            )
    if 'DIA' in sheets:
        dia_df = sheets['DIA']
        dia_df.columns = dia_df.columns.str.strip()
        dia_df = dia_df.fillna(0)  # Substitui NaN por 0

        for _, row in dia_df.iterrows():
            EscalaDia.objects.update_or_create(
                frota=row['FROTA'],
                placa=row['PLACA'],
                defaults={
                    'descricao': row['DESCRIÇÃO'],
                    'matricula': row['MATRÍCULA'],
                    'colaborador': row['COLABORADOR - DIA'],
                    'workday': row['WORKDAY'],
                    'admissao': row['ADMISSÃO'],
                    'ferias': row.get('FÉRIAS', ''),
                    'contato': row.get('CONTATO', ''),
                    'letra': row['LETRA'],
                    'horario': row['HORÁRIO'],
                }
            )

    if 'NOITE' in sheets:
        noite_df = sheets['NOITE']
        noite_df.columns = noite_df.columns.str.strip()
        noite_df = noite_df.fillna(0)  # Substitui NaN por 0

        for _, row in noite_df.iterrows():
            EscalaNoite.objects.update_or_create(
                frota=row['FROTA'],
                placa=row['PLACA'],
                defaults={
                    'descricao': row['DESCRIÇÃO'],
                    'matricula': row['MATRÍCULA'],
                    'colaborador': row['COLABORADOR - NOITE'],
                    'workday': row['WORKDAY'],
                    'admissao': row['ADMISSÃO'],
                    'ferias': row.get('FÉRIAS', ''),
                    'contato': row.get('CONTATO', ''),
                    'letra': row['LETRA'],
                    'horario': row['HORÁRIO'],
                }
            )
                
                