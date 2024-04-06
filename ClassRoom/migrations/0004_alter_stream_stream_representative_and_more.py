# Generated by Django 5.0.4 on 2024-04-06 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassRoom', '0003_alter_room_room_representative_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='stream_representative',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClassRoom.parent'),
        ),
        migrations.AlterField(
            model_name='stream',
            name='stream_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ClassRoom.teacher'),
        ),
    ]
