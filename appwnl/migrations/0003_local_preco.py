# Generated by Django 2.2.6 on 2019-10-30 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appwnl', '0002_remove_local_preco'),
    ]

    operations = [
        migrations.AddField(
            model_name='local',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
