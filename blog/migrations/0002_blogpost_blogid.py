# Generated by Django 4.2 on 2023-08-20 16:18

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blogid',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
