# Generated by Django 3.2.6 on 2024-04-09 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
