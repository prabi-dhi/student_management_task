# Generated by Django 5.1.3 on 2024-11-18 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
