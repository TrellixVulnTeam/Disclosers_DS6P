# Generated by Django 3.1.4 on 2020-12-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseobject',
            name='db_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
