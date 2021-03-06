# Generated by Django 2.2.2 on 2019-06-17 11:14

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('views', '0017_require_uri_prefix'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='view',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='view',
            name='sites',
            field=models.ManyToManyField(help_text='The sites this view belongs to (in a multi site setup).', to='sites.Site', verbose_name='Sites'),
        ),
    ]
