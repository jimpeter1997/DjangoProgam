# Generated by Django 2.2.6 on 2019-10-17 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191017_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productslist',
            name='pro_img_face',
            field=models.ImageField(upload_to='products_upload_images/'),
        ),
    ]
