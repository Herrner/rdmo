# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conditions', '0012_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='comment',
            field=models.TextField(blank=True, help_text='Additional internal information about this condition.', null=True, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='key',
            field=models.SlugField(blank=True, help_text='The internal identifier of this condition.', max_length=128, null=True, verbose_name='Key'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='relation',
            field=models.CharField(choices=[('eq', 'is equal to (==)'), ('neq', 'is not equal to (!=)'), ('contains', 'contains'), ('gt', 'is greater than (>)'), ('gte', 'is greater than or equal (>=)'), ('lt', 'is lesser than (<)'), ('lte', 'is lesser than or equal (<=)'), ('empty', 'is empty'), ('notempty', 'is not empty')], help_text='The Relation this condition is using.', max_length=8, verbose_name='Relation'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='source',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='The Attribute this condition is evaluating.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='domain.Attribute', verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='target_option',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='If using an options attribute, the option this condition is checking against.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='options.Option', verbose_name='Target (Option)'),
        ),
        migrations.AlterField(
            model_name='condition',
            name='target_text',
            field=models.CharField(blank=True, help_text='If using a regular attibute, the text value this condition is checking against.', max_length=256, null=True, verbose_name='Target (Text)'),
        ),
    ]