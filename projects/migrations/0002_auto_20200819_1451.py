# Generated by Django 3.1 on 2020-08-19 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=100),
        ),
    ]