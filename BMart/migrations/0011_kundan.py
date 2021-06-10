# Generated by Django 3.1.7 on 2021-05-07 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMart', '0010_panch'),
    ]

    operations = [
        migrations.CreateModel(
            name='kundan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('desc', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='images/')),
            ],
            options={
                'db_table': 'kundan',
            },
        ),
    ]
