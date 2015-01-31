# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0002_staff_advisory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='FIELDNAME',
            new_name='prefix',
        ),
    ]
