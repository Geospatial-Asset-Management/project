# Generated by Django 3.1.7 on 2021-05-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0021_auto_20210523_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='poylfield',
        ),
        migrations.AlterField(
            model_name='asset',
            name='elevation',
            field=models.CharField(blank=True, max_length=1111, null=True),
        ),
    ]