# Generated by Django 3.0 on 2020-02-05 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlapp', '0018_auto_20200204_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gameunit',
            name='status',
        ),
        migrations.AddField(
            model_name='gameunit',
            name='finish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gameunit',
            name='postpone',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gameunit',
            name='regular',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='teamunit',
            name='G',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teamunit',
            name='L',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teamunit',
            name='PCT',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='teamunit',
            name='W',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='gameunit',
            name='guestScore',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='gameunit',
            name='homeScore',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='guest1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='guest2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='guest3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='guest4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='guest5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='guest6',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='guest7',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='home1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='home2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='home3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='home4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='home5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='home6',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scoreunit',
            name='home7',
            field=models.IntegerField(null=True),
        ),
    ]
