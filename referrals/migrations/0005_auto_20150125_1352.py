# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0004_auto_20150125_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referral',
            old_name='FIELDNAME',
            new_name='consequence',
        ),
    ]
