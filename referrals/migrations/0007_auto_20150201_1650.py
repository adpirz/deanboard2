# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0006_auto_20150126_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
