# Generated by Django 2.2 on 2019-04-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='id',
        ),
        migrations.AddField(
            model_name='test',
            name='subscriber_key',
            field=models.CharField(default='asdf', max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
