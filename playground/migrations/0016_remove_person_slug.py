# Generated by Django 3.2 on 2022-03-08 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0015_alter_person_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='slug',
        ),
    ]
