# Generated by Django 5.0.2 on 2024-11-14 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('sub_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('sub_name', models.TextField(max_length=50)),
                ('teacher_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
        ),
    ]
