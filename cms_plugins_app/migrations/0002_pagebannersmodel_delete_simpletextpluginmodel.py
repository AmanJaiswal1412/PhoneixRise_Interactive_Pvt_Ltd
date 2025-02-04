# Generated by Django 5.1.1 on 2024-09-22 07:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0035_auto_20230822_2208_squashed_0036_auto_20240311_1028'),
        ('cms_plugins_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageBannersModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('alt_tag', models.CharField(default='Page', max_length=100)),
                ('banner_images', models.ImageField(upload_to='static/images/page_banners')),
                ('page_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='linked_pages', to='cms.page', verbose_name='Page')),
            ],
            bases=('cms.cmsplugin',),
        ),
        migrations.DeleteModel(
            name='SimpleTextPluginModel',
        ),
    ]
