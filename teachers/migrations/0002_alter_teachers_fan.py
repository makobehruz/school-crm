# Generated by Django 5.1.4 on 2025-01-06 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_remove_subject_rahbar'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='fan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='subjects.subject'),
        ),
    ]
