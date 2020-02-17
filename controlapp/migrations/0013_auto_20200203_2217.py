# Generated by Django 3.0 on 2020-02-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlapp', '0012_auto_20200203_2147'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('modify', models.DateTimeField(auto_now=True)),
                ('press', models.IntegerField(default=0)),
                ('publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='pitcherunit',
            name='CG',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pitcherunit',
            name='SHO',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pitcherunit',
            name='no_walks',
            field=models.BooleanField(default=False),
        ),
    ]
