# Generated by Django 4.2.3 on 2023-08-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Opiniones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='detalle',
            field=models.CharField(max_length=1024),
        ),
    ]
