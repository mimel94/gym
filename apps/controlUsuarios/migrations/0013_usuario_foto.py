# Generated by Django 2.0 on 2021-09-22 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlUsuarios', '0012_usuario_rutina'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(null=True, upload_to='sitios', verbose_name='Foto'),
        ),
    ]
