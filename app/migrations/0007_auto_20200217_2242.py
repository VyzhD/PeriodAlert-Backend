# Generated by Django 2.2 on 2020-02-17 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200211_1243'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='Alert',
        ),
    ]