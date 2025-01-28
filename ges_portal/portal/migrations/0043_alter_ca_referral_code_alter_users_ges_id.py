# Generated by Django 5.1.4 on 2025-01-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0042_alter_ca_referral_code_alter_users_ges_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='referral_code',
            field=models.CharField(default='8f64', max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='ges_id',
            field=models.CharField(blank=True, default='GES6150', max_length=10, unique=True),
        ),
    ]
