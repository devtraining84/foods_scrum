# Generated by Django 2.2.6 on 2020-02-21 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jedzonko', '0003_auto_20200219_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='method_preparation',
            field=models.TextField(null=True),
        ),
    ]
