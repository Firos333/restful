# Generated by Django 3.0.5 on 2020-05-07 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarytable',
            name='date_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='primarytable',
            name='time_modified',
            field=models.TimeField(auto_now=True),
        ),
    ]