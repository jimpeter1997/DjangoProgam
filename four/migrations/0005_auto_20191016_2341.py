# Generated by Django 2.2.6 on 2019-10-16 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('four', '0004_auto_20191016_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fourinfo',
            name='four_detail_words',
            field=models.TextField(max_length=500),
        ),
    ]
