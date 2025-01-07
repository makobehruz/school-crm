# Generated by Django 5.1.4 on 2025-01-07 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_alter_students_guruh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='students',
            name='rasm',
            field=models.ImageField(upload_to='student_image/'),
        ),
        migrations.AlterField(
            model_name='students',
            name='telefon',
            field=models.CharField(max_length=13),
        ),
    ]