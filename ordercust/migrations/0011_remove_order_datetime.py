# Generated by Django 3.1.7 on 2021-03-03 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordercust', '0010_auto_20210303_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='datetime',
        ),
    ]
