# Generated by Django 3.1.7 on 2021-05-22 16:20

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asset_Life_Cycle', '0003_auto_20210522_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifecyclephase',
            name='color',
            field=colorfield.fields.ColorField(blank=True, choices=[('#FFFFFF90', 'white'), ('#00000090', 'black'), ('#80808090', 'grey'), ('#FFFF0090', 'yellow'), ('#FF000090', 'red'), ('#0000FF90', 'blue'), ('#00800090', 'green'), ('#FFC0CB90', 'pink')], default='#FFFFFFFF', max_length=18, null=True),
        ),
    ]
