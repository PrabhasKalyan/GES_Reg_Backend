# Generated by Django 5.1.4 on 2025-01-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0033_remove_users_ges_id_alter_ca_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='referral_code',
            field=models.CharField(default='9501', max_length=4, unique=True),
        ),
    ]
