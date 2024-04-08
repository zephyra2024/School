# Generated by Django 5.0.4 on 2024-04-06 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=255, unique=True)),
                ('room_count', models.PositiveIntegerField(default=0)),
                ('room_representative', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClassRoom.parent')),
                ('room_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClassRoom.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('stream_id', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('stream_name', models.CharField(max_length=255, unique=True)),
                ('stream_prefect', models.CharField(blank=True, max_length=255, null=True)),
                ('stream_count', models.PositiveIntegerField(default=0)),
                ('stream_representative', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClassRoom.parent')),
                ('stream_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ClassRoom.room')),
                ('stream_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClassRoom.teacher')),
            ],
        ),
    ]
