# Generated by Django 2.2.6 on 2020-06-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20200620_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_id',
            field=models.CharField(default='no id', max_length=9, unique=True),
        ),
    ]
