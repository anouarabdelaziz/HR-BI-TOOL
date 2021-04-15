# Generated by Django 3.0.8 on 2021-04-08 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume1', '0005_auto_20210409_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='comp',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='comp',
            name='importance',
            field=models.IntegerField(choices=[('REQUIRED', 1), ('SECONDARY', 2), ('PLUS', 3)], default='REQUIRED'),
        ),
    ]
