# Generated by Django 2.2.6 on 2020-06-20 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='name',
            field=models.CharField(default='jay', max_length=50),
        ),
    ]
