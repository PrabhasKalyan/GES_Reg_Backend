# Generated by Django 5.1.4 on 2025-01-23 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0026_alter_ca_referral_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='ges_id',
        ),
        migrations.AlterField(
            model_name='ca',
            name='referral_code',
            field=models.CharField(default='635e', max_length=4, unique=True),
        ),
    ]
