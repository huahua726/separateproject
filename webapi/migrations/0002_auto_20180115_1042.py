# Generated by Django 2.0.1 on 2018-01-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
