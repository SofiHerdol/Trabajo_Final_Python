# Generated by Django 4.1.4 on 2023-01-10 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_app', '0002_animalshelter_animals_exotic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.FloatField(max_length=3)),
                ('dni', models.FloatField(max_length=15)),
                ('house', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='animals',
            name='baby',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='animalshelter',
            name='contact_number',
            field=models.FloatField(default='None'),
        ),
        migrations.AlterField(
            model_name='animals',
            name='age',
            field=models.FloatField(max_length=3),
        ),
    ]