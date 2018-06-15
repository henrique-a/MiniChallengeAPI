# Generated by Django 2.0.6 on 2018-06-15 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180614_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingridient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(default='', max_length=50)),
                ('quantity', models.FloatField(default=1.0)),
                ('unity', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingridients',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Ingridient'),
        ),
    ]
