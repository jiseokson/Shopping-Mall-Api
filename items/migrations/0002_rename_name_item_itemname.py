# Generated by Django 5.0.6 on 2024-06-27 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='itemname',
        ),
    ]
