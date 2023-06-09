# Generated by Django 4.2.1 on 2023-05-30 16:39

from django.db import migrations


def kategoria_feltolt(apps, schema_editor):
    Kategoria = apps.get_model("app", "Kategoria")
    kategoria_lista = ['torta', 'fagyi', 'egyeb']
    
    for i in range(len(kategoria_lista)):
        k = Kategoria(i + 1, kategoria_lista[i])
        k.save()


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(kategoria_feltolt)
    ]
