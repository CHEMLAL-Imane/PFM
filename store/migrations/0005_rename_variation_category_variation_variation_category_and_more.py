# Generated by Django 4.2.7 on 2024-01-10 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='Variation_CATEGORY',
            new_name='variation_category',
        ),
        migrations.RenameField(
            model_name='variation',
            old_name='Variation_value',
            new_name='variation_value',
        ),
    ]
