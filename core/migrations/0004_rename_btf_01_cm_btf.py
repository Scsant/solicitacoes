# Generated by Django 5.1.2 on 2024-12-14 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_cm_escala_pranchas_tritrem"),
    ]

    operations = [
        migrations.RenameField(model_name="cm", old_name="btf_01", new_name="btf",),
    ]
