# Generated by Django 3.0.8 on 2020-11-23 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0018_delete_userdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newitem',
            old_name='item_veg',
            new_name='item_type',
        ),
    ]