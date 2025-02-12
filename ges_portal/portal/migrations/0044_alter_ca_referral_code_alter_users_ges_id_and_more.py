# Generated by Django 5.1.4 on 2025-01-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0043_alter_ca_referral_code_alter_users_ges_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='referral_code',
            field=models.CharField(default='973e', max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='ges_id',
            field=models.CharField(blank=True, default='GESA7A3', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
    ]
