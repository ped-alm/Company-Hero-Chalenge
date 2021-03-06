# Generated by Django 3.1.1 on 2020-09-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('employee', '0002_auto_20200906_1844'),
        ('company', '0003_auto_20200906_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='employees',
            field=models.ManyToManyField(blank=True, null=True, to='employee.Employee'),
        ),
        migrations.AlterField(
            model_name='company',
            name='trading_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
