# Generated by Django 2.1.7 on 2019-04-25 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_info', '0002_auto_20190424_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieinfo',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]