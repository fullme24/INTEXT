# Generated by Django 3.1.2 on 2020-12-08 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20201208_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='skillName',
            field=models.CharField(max_length=50),
        ),
    ]
