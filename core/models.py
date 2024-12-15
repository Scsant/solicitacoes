from django.db import models

class Solicitation(models.Model):
    object_id = models.BigIntegerField()  # objectid
    global_id = models.UUIDField()  # globalid
    menu = models.CharField(max_length=255)  # menu
    date = models.DateTimeField(null=True, blank=True)  # data_
    responsible_collaborator = models.CharField(max_length=255)  # colaborador_responsavel
    equipment = models.CharField(max_length=255)  # equipamento
    equipment_quantity = models.IntegerField(null=True, blank=True)  # qnt_equipamento
    cc_module = models.CharField(max_length=100)  # cc_modulo
    quantity = models.IntegerField(null=True, blank=True)  # quantidade
    axles = models.IntegerField(null=True, blank=True)  # eixos
    request = models.TextField(null=True, blank=True)  # solicitacao
    rescheduling = models.FloatField(null=True, blank=True)  # reprogramacao
    cancellation = models.TextField(null=True, blank=True)  # cancelamento
    equipment_id = models.FloatField(null=True, blank=True)  # id_equip
    reservation_date = models.DateTimeField(null=True, blank=True)  # data_reserva
    calc_date = models.CharField(max_length=100, null=True, blank=True)  # data_calc
    reservation_time = models.CharField(max_length=50, null=True, blank=True)  # hora_reserva
    calc_time = models.CharField(max_length=50, null=True, blank=True)  # hora_calc
    origin_farm = models.CharField(max_length=255, null=True, blank=True)  # fazenda_origem
    destination_farm = models.CharField(max_length=255, null=True, blank=True)  # fazenda_destino
    center_1 = models.FloatField(null=True, blank=True)  # centro_1
    observation = models.TextField(null=True, blank=True)  # observ
    reservation_id = models.CharField(max_length=100, null=True, blank=True)  # id_reserva
    created_date = models.DateTimeField(null=True, blank=True)  # created_date
    last_edited_date = models.DateTimeField(null=True, blank=True)  # last_edited_date
    x_coordinate = models.FloatField(null=True, blank=True)  # x
    y_coordinate = models.FloatField(null=True, blank=True)  # y

    def __str__(self):
        return f"Solicitação {self.global_id} - {self.equipment}"

from django.db import models

class CM(models.Model):
    quantidade = models.IntegerField()
    btf = models.IntegerField() 

# Modelo para a aba PRANCHAS
class Pranchas(models.Model):
    quan = models.IntegerField()
    frota = models.IntegerField()
    placa = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    especificacoes = models.TextField()
    chassis = models.CharField(max_length=100)

# Modelo para a aba TRITREM
class Tritrem(models.Model):
    btf_01 = models.IntegerField()
    placa = models.CharField(max_length=50)
    primeira_carreta = models.CharField(max_length=50)
    segunda_carreta = models.CharField(max_length=50)
    terceira_carreta = models.CharField(max_length=50)
    fabricante_cm = models.CharField(max_length=100)
    fabricante_conjunto = models.CharField(max_length=100)

class EscalaDia(models.Model):
    frota = models.CharField(max_length=255)  # FROTA
    placa = models.CharField(max_length=255)  # PLACA
    descricao = models.CharField(max_length=255)  # DESCRIÇÃO
    matricula = models.BigIntegerField()  # MATRÍCULA
    colaborador = models.CharField(max_length=255)  # COLABORADOR - DIA
    workday = models.FloatField(null=True, blank=True)  # WORKDAY
    admissao = models.DateField(null=True, blank=True)  # ADMISSÃO
    ferias = models.CharField(max_length=255, null=True, blank=True)  # FÉRIAS
    contato = models.CharField(max_length=255, null=True, blank=True)  # CONTATO
    letra = models.CharField(max_length=10)  # LETRA
    horario = models.CharField(max_length=50)  # HORÁRIO

    def __str__(self):
        return f"{self.colaborador} ({self.frota}) - DIA"


class EscalaNoite(models.Model):
    frota = models.CharField(max_length=255)  # FROTA
    placa = models.CharField(max_length=255)  # PLACA
    descricao = models.CharField(max_length=255)  # DESCRIÇÃO
    matricula = models.BigIntegerField()  # MATRÍCULA
    colaborador = models.CharField(max_length=255)  # COLABORADOR - NOITE
    workday = models.FloatField(null=True, blank=True)  # WORKDAY
    admissao = models.DateField(null=True, blank=True)  # ADMISSÃO
    ferias = models.CharField(max_length=255, null=True, blank=True)  # FÉRIAS
    contato = models.CharField(max_length=255, null=True, blank=True)  # CONTATO
    letra = models.CharField(max_length=10)  # LETRA
    horario = models.CharField(max_length=50)  # HORÁRIO

    def __str__(self):
        return f"{self.colaborador} ({self.frota}) - NOITE"



