# Generated by Django 4.1.2 on 2022-11-01 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accounts',
            name='fullname',
        ),
    ]
