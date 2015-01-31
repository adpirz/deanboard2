# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('grade', models.IntegerField(choices=[(5, b'5'), (6, b'6'), (7, b'7'), (8, b'8')])),
            ],
            options={
                'verbose_name': 'Advisory',
                'verbose_name_plural': 'Advisories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('reason', models.CharField(max_length=100, choices=[(b'Repeated', b'Repeated Infractions'), (b'Walkout', b'Walked out'), (b'Ignored', b'Walked Away/Ignored'), (b'Language', b'Abusive/Profane Language'), (b'Bullying', b'Threatening/Bullying'), (b'Harassment', b'Harassment (sexual, racial, etc.)'), (b'Preventing', b'Preventing continuation of class'), (b'Response', b'Inappropriate response to a consequence'), (b'Horseplay', b'Horseplay'), (b'Fight', b'Fight')])),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Referral',
                'verbose_name_plural': 'Referrals',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('grade', models.IntegerField(choices=[(5, b'5'), (6, b'6'), (7, b'7'), (8, b'8')])),
                ('advisory', models.ForeignKey(to='referrals.Advisory')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('FIELDNAME', models.CharField(max_length=4, choices=[(b'Mr.', b'Mr.'), (b'Ms.', b'Ms.'), (b'Mrs.', b'Mrs.')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='referral',
            name='scholar',
            field=models.ForeignKey(to='referrals.Scholar'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='referral',
            name='staff',
            field=models.ForeignKey(to='referrals.Staff'),
            preserve_default=True,
        ),
    ]
