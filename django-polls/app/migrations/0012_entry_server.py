# Generated by Django 2.0.5 on 2018-07-06 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_server'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry_server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('ip', models.CharField(default='0.0.0', max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='app.Server')),
            ],
            options={
                'verbose_name_plural': 'ip_name',
            },
        ),
    ]
