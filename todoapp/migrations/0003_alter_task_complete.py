# Generated by Django 4.0.5 on 2022-07-04 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_complete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
