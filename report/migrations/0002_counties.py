# Generated by Django 2.2.2 on 2020-01-31 10:04

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Counties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=2)),
                ('division', models.CharField(max_length=2)),
                ('statefp', models.CharField(max_length=2)),
                ('statens', models.CharField(max_length=8)),
                ('geoid', models.CharField(max_length=2)),
                ('stusps', models.CharField(max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('lsad', models.CharField(max_length=2)),
                ('mtfcc', models.CharField(max_length=5)),
                ('funcstat', models.CharField(max_length=1)),
                ('aland', models.BigIntegerField()),
                ('awater', models.BigIntegerField()),
                ('intptlat', models.CharField(max_length=11)),
                ('intptlon', models.CharField(max_length=12)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
