# Generated by Django 2.2.16 on 2020-12-13 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=256)),
                ('counter', models.PositiveIntegerField(default=1)),
            ],
        ),
    ]
