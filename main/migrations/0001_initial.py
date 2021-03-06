# Generated by Django 3.2.7 on 2021-09-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=50, unique=True)),
                ('time', models.DateField(auto_now_add=True)),
                ('numberOfResult', models.IntegerField()),
            ],
        ),
    ]
