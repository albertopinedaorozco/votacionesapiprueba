# Generated by Django 3.0.6 on 2020-06-01 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locaciones', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ciudad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locaciones.Municipio'),
        ),
        migrations.AddField(
            model_name='user',
            name='direccion',
            field=models.CharField(blank=True, max_length=70),
        ),
    ]
