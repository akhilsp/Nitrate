# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-24 02:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issuetracker', '0011_modify_issuetracker_issue_report_fields'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='issue',
            unique_together=set([('tracker', 'issue_key')]),
        ),
    ]