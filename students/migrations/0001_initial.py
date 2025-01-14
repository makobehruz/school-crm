# Generated by Django 5.1.4 on 2024-12-25 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=100)),
                ('familiya', models.CharField(max_length=100)),
                ('guruh', models.CharField(max_length=25)),
                ('telefon', models.PositiveIntegerField(max_length=20)),
                ('rasm', models.ImageField(upload_to='student_image/')),
            ],
        ),
    ]
