# Generated by Django 3.1.3 on 2021-05-12 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Asset_Life_Cycle', '0001_initial'),
        ('crt_ast', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifecycle',
            name='asset_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt_ast.assettype'),
        ),
    ]
