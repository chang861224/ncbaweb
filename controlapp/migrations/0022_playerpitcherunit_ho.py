# Generated by Django 3.0 on 2020-02-12 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlapp', '0021_gameunit_playoff'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerpitcherunit',
            name='HO',
            field=models.IntegerField(default=0),
        ),
    ]
