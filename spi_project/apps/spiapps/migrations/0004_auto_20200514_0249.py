# Generated by Django 2.1.15 on 2020-05-14 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spiapps', '0003_auto_20200514_0144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avref',
            old_name='PartNumber',
            new_name='PN',
        ),
    ]