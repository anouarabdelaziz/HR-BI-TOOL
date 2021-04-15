# Generated by Django 3.0.8 on 2021-04-04 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=50, null=True)),
                ('experience', models.PositiveIntegerField(blank=True, null=True)),
                ('Cv', models.FileField(upload_to='media/pdfs/')),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('Description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('importance', models.IntegerField(choices=[('REQUIRED', '1'), ('SECONDARY', '2'), ('PLUS', '3')], null=True)),
                ('recruit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='resume1.Recruit')),
            ],
        ),
    ]