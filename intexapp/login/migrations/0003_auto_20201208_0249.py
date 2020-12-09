# Generated by Django 3.1.2 on 2020-12-08 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20201208_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='joblistings',
            name='applicationsTable',
            field=models.ManyToManyField(related_name='user_job_applications', through='login.Applications', to='login.Person'),
        ),
        migrations.AlterField(
            model_name='joblistings',
            name='savedJobListings',
            field=models.ManyToManyField(related_name='user_saved_jobs', through='login.SavedJobs', to='login.Person'),
        ),
    ]