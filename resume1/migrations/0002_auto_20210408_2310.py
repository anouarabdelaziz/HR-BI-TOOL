# Generated by Django 3.0.8 on 2021-04-08 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='experience',
            field=models.CharField(blank=True, choices=[('less then one year', '1'), ('between two and three years', '3'), ('between three and five years', '5'), ('between five and ten years', '7'), ('more then ten years', '10')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comp',
            name='importance',
            field=models.CharField(choices=[('REQUIRED', '1'), ('SECONDARY', '2'), ('PLUS', '3')], max_length=20, null=True),
        ),
    ]