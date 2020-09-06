# Generated by Django 3.1.1 on 2020-09-06 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('rg', models.CharField(max_length=31)),
                ('cpf', models.CharField(max_length=31)),
                ('telephone', models.CharField(max_length=31)),
                ('email', models.CharField(max_length=255)),
                ('job', models.CharField(max_length=255)),
            ],
        ),
    ]
