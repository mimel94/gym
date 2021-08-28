# Generated by Django 2.0 on 2021-08-28 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlUsuarios', '0003_auto_20210821_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='entrenador',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='ocupacion',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='plan',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='controlUsuarios.Plan'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='sucursal',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='controlUsuarios.Sucursal'),
        ),
    ]
