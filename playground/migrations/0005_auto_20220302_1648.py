# Generated by Django 3.2 on 2022-03-02 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0004_auto_20220302_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='msgs',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.TextField(max_length=3),
        ),
        migrations.AlterField(
            model_name='person',
            name='reakcje',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='stopy',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='person',
            name='zdj',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
