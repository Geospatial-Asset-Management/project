# Generated by Django 3.1.3 on 2021-04-21 12:40

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Asset_Life_Cycle', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(srid=4326)),
                ('elevation', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='asset_photo/')),
                ('comissioning_date', models.DateField(blank=True, null=True)),
                ('decommission_date', models.DateField(blank=True, null=True)),
                ('active', models.CharField(blank=True, choices=[('Yes', 'Active'), ('No', 'Inactive'), ('Maintenance', 'Maintenance')], max_length=11, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('markersize', models.CharField(blank=True, max_length=7, null=True)),
                ('markercolor', models.CharField(blank=True, max_length=7, null=True)),
                ('markersymbol', models.CharField(blank=True, max_length=15, null=True)),
                ('lc_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Asset_Life_Cycle.lifecyclephase')),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('industry', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=75)),
                ('office_location', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=75, null=True)),
                ('phone', models.IntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MaxValueValidator(99999999999999999)])),
                ('office_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crt_ast.office')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssetTypeSymbol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.ImageField(unique=True, upload_to='symbol_img/')),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt_ast.assettype')),
            ],
        ),
        migrations.CreateModel(
            name='AssetTypeProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('dtype', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt_ast.assettype')),
            ],
        ),
        migrations.CreateModel(
            name='AssetPropertyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=256)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt_ast.asset')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt_ast.assettypeproperty')),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crt_ast.assettype'),
        ),
    ]
