# Generated by Django 5.1.1 on 2024-09-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_plugins_app', '0003_remove_pagebannersmodel_alt_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagebannersmodel',
            name='banner_images',
            field=models.ImageField(upload_to='../images/page_banners'),
        ),
    ]
