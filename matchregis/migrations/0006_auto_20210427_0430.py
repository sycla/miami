# Generated by Django 3.1.7 on 2021-04-26 23:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matchregis', '0005_duomatchregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matchregistration',
            name='duocharacterid1',
        ),
        migrations.RemoveField(
            model_name='matchregistration',
            name='duocharacterid2',
        ),
        migrations.RemoveField(
            model_name='matchregistration',
            name='duophone',
        ),
        migrations.RemoveField(
            model_name='matchregistration',
            name='duotransid',
        ),
    ]