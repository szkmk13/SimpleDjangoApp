# Generated by Django 4.1.3 on 2022-11-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0009_word_chatmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatmessage',
            name='message',
            field=models.CharField(default='', max_length=200),
        ),
    ]