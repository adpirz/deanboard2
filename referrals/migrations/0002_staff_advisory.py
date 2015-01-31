# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='advisory',
            field=models.ForeignKey(default=2, to='referrals.Advisory'),
            preserve_default=False,
        ),
    ]
