# Generated by Django 5.1 on 2024-09-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('code', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=50)),
            ],
        ),
    ]
