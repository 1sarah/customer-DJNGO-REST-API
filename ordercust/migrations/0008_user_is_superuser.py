# Generated by Django 3.1.7 on 2021-03-02 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordercust', '0007_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]