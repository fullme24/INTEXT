# Generated by Django 3.1.2 on 2020-12-09 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20201208_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='personTypeID',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='login.persontype'),
        ),
    ]
