# Generated by Django 2.2.6 on 2019-10-18 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191017_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='productslist',
            name='pro_time',
            field=models.TimeField(null=True),
        ),
    ]
