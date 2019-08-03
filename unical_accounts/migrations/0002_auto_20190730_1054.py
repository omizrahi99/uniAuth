# Generated by Django 2.2.2 on 2019-07-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unical_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='origin',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='from which conenctor this user come from'),
        ),
        migrations.AddField(
            model_name='user',
            name='original_uid',
            field=models.CharField(blank=True, max_length=60, null=True, verbose_name='Username used in connectors auth'),
        ),
        migrations.AlterField(
            model_name='user',
            name='persistent_id',
            field=models.CharField(blank=True, max_length=254, null=True, verbose_name='SAML Persistent Stored ID'),
        ),
    ]