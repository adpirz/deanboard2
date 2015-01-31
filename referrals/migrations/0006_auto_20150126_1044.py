# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0005_auto_20150125_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='referral',
            options={'ordering': ['-datetime', 'scholar'], 'verbose_name': 'Referral', 'verbose_name_plural': 'Referrals'},
        ),
        migrations.AlterField(
            model_name='referral',
            name='consequence',
            field=models.CharField(default=b'DET', max_length=3, blank=True, choices=[(b'ISS', b'In School Suspension'), (b'DET', b'Detention'), (b'B2C', b'Back to Class'), (b'INV', b'Investigation')]),
        ),
        migrations.AlterField(
            model_name='referral',
            name='description',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
