# Generated by Django 3.2.17 on 2023-02-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee_data', '0002_auto_20230216_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='Employee_Profile_Photo',
            field=models.ImageField(default=True, upload_to='Employee_data/media'),
        ),
    ]
