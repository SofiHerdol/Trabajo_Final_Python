# Generated by Django 4.1.4 on 2023-02-08 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animal_app', '0020_userprofile_contact_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='user',
        ),
        migrations.DeleteModel(
            name='ContactNumber',
        ),
        migrations.DeleteModel(
            name='Avatar',
        ),
    ]
