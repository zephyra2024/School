# Generated by Django 5.0.4 on 2024-04-12 07:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassRoom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('name', models.CharField(max_length=22, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='stream',
            name='stream_prefect',
            field=models.ForeignKey(blank=True, max_length=255, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClassRoom.student'),
        ),
    ]
