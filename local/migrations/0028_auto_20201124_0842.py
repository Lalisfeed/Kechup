# Generated by Django 3.0.8 on 2020-11-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0027_auto_20201123_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newitem',
            name='item_label',
            field=models.CharField(max_length=64, null=True),
        ),
    ]