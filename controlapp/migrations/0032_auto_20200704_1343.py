# Generated by Django 3.0.8 on 2020-07-04 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlapp', '0031_gameunit_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='gameunit',
            name='year',
            field=models.IntegerField(default=108),
        ),
        migrations.AddField(
            model_name='playerunit',
            name='year',
            field=models.IntegerField(default=108),
        ),
        migrations.AddField(
            model_name='teamunit',
            name='year',
            field=models.IntegerField(default=108),
        ),
    ]