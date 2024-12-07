# Generated by Django 5.1.2 on 2024-12-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Solicitation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("object_id", models.BigIntegerField()),
                ("global_id", models.UUIDField()),
                ("menu", models.CharField(max_length=255)),
                ("date", models.DateTimeField()),
                ("responsible_collaborator", models.CharField(max_length=255)),
                ("equipment", models.CharField(max_length=255)),
                ("equipment_quantity", models.IntegerField()),
                ("cc_module", models.CharField(max_length=100)),
                ("quantity", models.IntegerField()),
                ("axles", models.IntegerField()),
                ("request", models.TextField()),
                ("rescheduling", models.FloatField(blank=True, null=True)),
                ("cancellation", models.TextField(blank=True, null=True)),
                ("equipment_id", models.FloatField(blank=True, null=True)),
                ("reservation_date", models.DateTimeField()),
                ("calc_date", models.CharField(max_length=100)),
                ("reservation_time", models.CharField(max_length=50)),
                ("calc_time", models.CharField(max_length=50)),
                ("origin_farm", models.CharField(max_length=255)),
                ("destination_farm", models.CharField(max_length=255)),
                ("center_1", models.FloatField(blank=True, null=True)),
                ("observation", models.TextField(blank=True, null=True)),
                ("reservation_id", models.CharField(max_length=100)),
                ("created_date", models.DateTimeField()),
                ("last_edited_date", models.DateTimeField()),
                ("x_coordinate", models.FloatField()),
                ("y_coordinate", models.FloatField()),
            ],
        ),
    ]
