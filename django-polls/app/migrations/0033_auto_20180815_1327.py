# Generated by Django 2.0.5 on 2018-08-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20180815_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='check_instance10',
            field=models.CharField(default='check_instance10', max_length=500),
        ),
        migrations.AddField(
            model_name='server',
            name='check_instance9',
            field=models.CharField(default='check_instance9', max_length=500),
        ),
        migrations.AlterField(
            model_name='server',
            name='check_instance5',
            field=models.CharField(default='check_instance5', max_length=500),
        ),
        migrations.AlterField(
            model_name='server',
            name='check_instance8',
            field=models.CharField(default='check_instance8', max_length=500),
        ),
    ]