# Generated by Django 2.1.15 on 2020-05-14 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spiapps', '0002_auto_20200514_0143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avref',
            old_name='PN',
            new_name='PartNumber',
        ),
    ]