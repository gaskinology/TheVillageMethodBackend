# Generated by Django 3.0.8 on 2020-07-21 23:04

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('institution_type', models.CharField(default='', max_length=30)),
                ('school_id', models.IntegerField(default=0)),
                ('city', models.CharField(default='', max_length=100)),
                ('state', models.CharField(default='', max_length=2)),
                ('website_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='academic_years',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=7), default=list, size=None),
        ),
        migrations.AddField(
            model_name='course',
            name='ag_designation',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AddField(
            model_name='course',
            name='course_length',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='course',
            name='grade_levels',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=list, size=None),
        ),
        migrations.AddField(
            model_name='course',
            name='is_honors',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='provider',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='transcript_abbs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=50), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='school',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.School'),
        ),
    ]
