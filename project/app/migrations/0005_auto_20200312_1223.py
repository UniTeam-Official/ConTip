# Generated by Django 3.0.3 on 2020-03-12 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200312_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
