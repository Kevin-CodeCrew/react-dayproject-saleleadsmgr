# Generated by Django 2.2.3 on 2019-11-06 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lead_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesleadmodel',
            old_name='company',
            new_name='companyFk',
        ),
        migrations.RenameField(
            model_name='salesleadmodel',
            old_name='user',
            new_name='userFk',
        ),
    ]
