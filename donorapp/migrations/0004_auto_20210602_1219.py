# Generated by Django 3.2 on 2021-06-02 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donorapp', '0003_auto_20210413_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='city',
            name='state',
        ),
        migrations.RemoveField(
            model_name='donor',
            name='state',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
