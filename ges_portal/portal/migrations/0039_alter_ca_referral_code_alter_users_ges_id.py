# Generated by Django 5.1.4 on 2025-01-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0038_alter_ca_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='referral_code',
            field=models.CharField(default='d487', max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='ges_id',
            field=models.CharField(blank=True, default='GESE5474B', max_length=10, unique=True),
        ),
    ]
