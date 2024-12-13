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


