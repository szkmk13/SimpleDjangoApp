# Generated by Django 3.2 on 2022-03-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240, verbose_name='Name')),
                ('email', models.EmailField(max_length=254)),
                ('document', models.CharField(max_length=20, verbose_name='Document')),
                ('phone', models.CharField(max_length=20)),
                ('registrationDate', models.DateField(auto_now_add=True, verbose_name='Registration Date')),
            ],
        ),
    ]
