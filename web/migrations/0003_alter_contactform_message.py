# Generated by Django 5.0.6 on 2024-07-21 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
