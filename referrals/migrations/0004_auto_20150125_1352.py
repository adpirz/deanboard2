# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0003_auto_20150125_0638'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='FIELDNAME',
            field=models.CharField(default=b'DET', max_length=3, choices=[(b'ISS', b'In School Suspension'), (b'DET', b'Detention'), (b'B2C', b'Back to Class'), (b'INV', b'Investigation')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='referral',
            name='in_dos',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
