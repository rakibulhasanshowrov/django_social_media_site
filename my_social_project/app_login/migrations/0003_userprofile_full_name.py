# Generated by Django 4.2 on 2024-06-24 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0002_alter_userprofile_dob_alter_userprofile_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=264),
        ),
    ]
