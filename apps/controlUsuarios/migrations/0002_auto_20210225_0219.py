# Generated by Django 2.0 on 2021-02-25 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlUsuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='numero_documento',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
