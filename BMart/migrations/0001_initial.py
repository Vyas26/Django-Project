# Generated by Django 3.1.7 on 2021-05-06 17:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='om',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='images/')),
            ],
            options={
                'db_table': 'om',
            },
        ),
        migrations.CreateModel(
            name='pj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='images/')),
            ],
            options={
                'db_table': 'pj',
            },
        ),
        migrations.CreateModel(
            name='RegIns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'registration',
            },
        ),
        migrations.CreateModel(
            name='sgv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='images/')),
            ],
            options={
                'db_table': 'sgv',
            },
        ),
    ]
