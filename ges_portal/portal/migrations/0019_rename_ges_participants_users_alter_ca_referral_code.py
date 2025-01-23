# Generated by Django 5.1.4 on 2025-01-22 07:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0018_alter_ca_referral_code'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GES_Participants',
            new_name='Users',
        ),
        migrations.AlterField(
            model_name='ca',
            name='referral_code',
            field=models.CharField(default='447d', max_length=4, unique=True),
        ),
    ]
