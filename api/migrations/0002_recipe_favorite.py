# Generated by Django 2.0.6 on 2018-06-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
