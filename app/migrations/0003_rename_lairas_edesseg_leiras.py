# Generated by Django 4.2.1 on 2023-05-30 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_kategoria_Migration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='edesseg',
            old_name='lairas',
            new_name='leiras',
        ),
    ]
