# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0008_auto_20150215_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='reason',
            field=models.CharField(max_length=100, choices=[(b'Repeated', b'Repeated Infractions'), (b'Walkout', b'Walked out'), (b'Ignored', b'Walked Away/Ignored'), (b'Language', b'Abusive/Profane Language'), (b'Bullying', b'Threatening/Bullying'), (b'Harassment', b'Harassment (sexual, racial, etc.)'), (b'Preventing', b'Preventing continuation of class'), (b'Response', b'Inappropriate response to a consequence'), (b'Horseplay', b'Horseplay'), (b'Fight', b'Fight'), (b'Other', b'Other')]),
        ),
    ]
