# Generated by Django 4.2 on 2023-08-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogcomment_updatedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='UpdatedAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
