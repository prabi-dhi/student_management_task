# Generated by Django 5.1.3 on 2024-11-18 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_alter_classroom_total_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
