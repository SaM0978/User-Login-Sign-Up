# Generated by Django 4.2.1 on 2023-06-10 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCreation',
            fields=[
                ('userId', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=18)),
            ],
        ),
    ]
