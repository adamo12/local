# Generated by Django 2.0.5 on 2018-07-10 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Topic'),
        ),
    ]