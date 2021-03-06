# Generated by Django 3.1.7 on 2021-05-11 12:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMart', '0011_kundan'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_json', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
