# Generated by Django 4.2.16 on 2024-09-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_myuser_is_admin_myuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
