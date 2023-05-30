# Generated by Django 4.2.1 on 2023-05-30 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('kategoria_azon', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='kategoria_azon')),
                ('nev', models.CharField(max_length=50, verbose_name='kategoria_nev')),
            ],
        ),
        migrations.CreateModel(
            name='Edesseg',
            fields=[
                ('edesseg_azon', models.AutoField(editable=False, primary_key=True, serialize=False, verbose_name='edesseg_azon')),
                ('nev', models.CharField(max_length=50, verbose_name='edesseg_nev')),
                ('lairas', models.CharField(max_length=100, verbose_name='lairas')),
                ('ar', models.IntegerField(verbose_name='ar')),
                ('kep_utvonal', models.CharField(blank=True, max_length=60, null=True, verbose_name='kep_utvonal')),
                ('kategoria_azon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.kategoria', verbose_name='kategoria_azon_kulsokulcs')),
            ],
        ),
    ]
