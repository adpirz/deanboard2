# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0007_auto_20150201_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='consequence',
            field=models.CharField(blank=True, max_length=3, choices=[(b'ISS', b'In School Suspension'), (b'DET', b'Detention'), (b'B2C', b'Back to Class'), (b'INV', b'Investigation')]),
        ),
    ]
