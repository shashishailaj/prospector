# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 03:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import healthmeter.projectinfo.models
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
                ('is_osi_approved', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField(blank=True, default='')),
                ('business_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='projectinfo.BusinessUnit')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('website_url', models.URLField(blank=True, null=True)),
                ('governance', models.TextField(blank=True, default='')),
                ('description', models.TextField(blank=True, default='')),
                ('has_contributor_agreement', models.BooleanField(default=False)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('is_wip', models.BooleanField(default=True, verbose_name='Configuration in progress')),
                ('logo', models.ImageField(blank=True, null=True, upload_to=healthmeter.projectinfo.models.logo_path)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('business_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='projectinfo.BusinessUnit')),
                ('licenses', models.ManyToManyField(blank=True, null=True, related_name='projects', to='projectinfo.License')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='projectinfo.Project')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('tree', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='projectinfo.Project')),
            ],
            options={
                'ordering': ('date', 'version'),
            },
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('project', 'version')]),
        ),
    ]