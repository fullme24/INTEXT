# Generated by Django 3.1.2 on 2020-12-09 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_merge_20201209_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorytype',
            name='type',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='companyemployee',
            name='jobTitle',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='joblistings',
            name='jobTitle',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='person',
            name='aboutMe',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='facebook',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='jobExperience',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='lat',
            field=models.DecimalField(decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='linkedin',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='long',
            field=models.DecimalField(decimal_places=8, max_digits=11, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='minorityTypeID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.minoritytype'),
        ),
        migrations.AlterField(
            model_name='person',
            name='personTypeID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.persontype'),
        ),
        migrations.AlterField(
            model_name='person',
            name='profilePic',
            field=models.FileField(null=True, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='person',
            name='resumeID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.resumes'),
        ),
        migrations.AlterField(
            model_name='person',
            name='twitter',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterModelTable(
            name='minoritytype',
            table=None,
        ),
    ]