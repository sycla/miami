# Generated by Django 3.1.7 on 2021-04-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchregis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchregistration',
            name='duocharacterid1',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchregistration',
            name='duocharacterid2',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchregistration',
            name='duophone',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='matchregistration',
            name='duotransid',
            field=models.CharField(default=15, max_length=100),
            preserve_default=False,
        ),
    ]
