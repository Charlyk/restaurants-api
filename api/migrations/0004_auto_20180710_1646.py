# Generated by Django 2.0.7 on 2018-07-10 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180710_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='referral_id',
            new_name='place_id',
        ),
    ]