# Generated by Django 3.1.7 on 2021-05-23 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0017_mushroomspot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mushroomspot',
            name='name',
        ),
        migrations.AlterField(
            model_name='asset',
            name='geom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt_ast.mushroomspot'),
        ),
    ]
