# Generated by Django 2.2.6 on 2019-10-30 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appwnl', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='preco',
        ),
    ]
