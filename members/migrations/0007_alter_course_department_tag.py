# Generated by Django 5.0.6 on 2024-07-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_remove_course_units_course_unit_max_course_unit_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department_tag',
            field=models.CharField(max_length=255),
        ),
    ]
