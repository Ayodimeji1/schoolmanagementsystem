# Generated by Django 4.0.6 on 2022-07-09 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staffs',
            options={'ordering': ['name']},
        ),
    ]
