# Generated by Django 3.0.8 on 2021-04-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume1', '0007_auto_20210409_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='experience',
            field=models.CharField(choices=[('1', 'less then one year'), ('3', 'between two and three years'), ('5', 'between three and five years'), ('7', 'between five and ten years'), ('10', 'more then ten years')], max_length=50, null=True),
        ),
    ]
