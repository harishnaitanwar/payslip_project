# Generated by Django 3.2.17 on 2023-02-28 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_data', '0007_auto_20230228_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenses',
            name='id',
        ),
        migrations.AlterField(
            model_name='expenses',
            name='SrNo',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
