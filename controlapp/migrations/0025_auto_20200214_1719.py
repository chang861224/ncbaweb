# Generated by Django 3.0 on 2020-02-14 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlapp', '0024_orderguestunit_orderhomeunit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderguestunit',
            name='substitute1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderguestunit',
            name='substitute2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderguestunit',
            name='substitute3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderguestunit',
            name='substitute4',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderguestunit',
            name='substitute5',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderguestunit',
            name='substitute6',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderguestunit',
            name='substitute7',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderguestunit',
            name='substitute8',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='orderguestunit',
            name='substitute9',
            field=models.CharField(max_length=100, null=True),
        ),
    ]