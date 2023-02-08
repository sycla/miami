# Generated by Django 4.0.6 on 2022-08-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jetski',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientname', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ponton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientname', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='yacht',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientname', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=20)),
            ],
        ),
    ]