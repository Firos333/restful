# Generated by Django 3.0.5 on 2020-05-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20200507_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primarytable',
            name='beam_no',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='primarytable',
            name='loom_no',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='primarytable',
            name='piece_no',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='primarytable',
            name='set_no',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
