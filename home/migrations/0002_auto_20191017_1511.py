# Generated by Django 2.2.6 on 2019-10-17 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productslist',
            name='pro_img_face',
            field=models.ImageField(upload_to='static/products_upload_images/'),
        ),
    ]
