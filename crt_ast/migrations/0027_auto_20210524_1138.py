# Generated by Django 3.1.7 on 2021-05-24 08:38

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crt_ast', '0026_auto_20210524_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='markercolor',
            field=colorfield.fields.ColorField(blank=True, choices=[('#FFFFFF', 'white'), ('#000000', 'black'), ('#808080', 'grey'), ('#FFFF00', 'yellow'), ('#FF0000', 'red'), ('#0000FF', 'blue'), ('#008000', 'green'), ('#FFA500', 'orange'), ('#87CEEB', 'light blue')], default='#FFFFFF', max_length=18, null=True),
        ),
    ]
