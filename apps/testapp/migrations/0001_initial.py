# Generated by Django 2.2 on 2019-04-24 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direct', models.CharField(max_length=50)),
                ('methods', models.CharField(max_length=50)),
            ],
        ),
    ]
