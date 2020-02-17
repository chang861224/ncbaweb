# Generated by Django 3.0 on 2020-01-25 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controlapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('studentID', models.CharField(max_length=20)),
                ('dept', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=10)),
                ('bt', models.CharField(max_length=50)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controlapp.TeamUnit')),
            ],
        ),
    ]
