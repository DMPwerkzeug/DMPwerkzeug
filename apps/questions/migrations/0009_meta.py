# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-27 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_data_migration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionentity',
            options={'ordering': ('subsection__section__catalog__order', 'subsection__section__order', 'subsection__order', 'order'), 'verbose_name': 'Question entity', 'verbose_name_plural': 'Question entities'},
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='attribute_entity',
            field=models.ForeignKey(blank=True, help_text='The attribute/entity this question/questionset belongs to.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='domain.AttributeEntity', verbose_name='Attribute entity'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='order',
            field=models.IntegerField(default=0, help_text='The position of this question/questionset in lists.', verbose_name='Order'),
        ),
        migrations.AlterField(
            model_name='questionentity',
            name='subsection',
            field=models.ForeignKey(help_text='The section this question/questionset belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='questions.Subsection', verbose_name='Subsection'),
        ),
        migrations.AlterField(
            model_name='subsection',
            name='section',
            field=models.ForeignKey(help_text='The section this subsection belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='subsections', to='questions.Section', verbose_name='Section'),
        ),
    ]
