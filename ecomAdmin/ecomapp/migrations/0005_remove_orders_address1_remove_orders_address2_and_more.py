# Generated by Django 4.2.5 on 2023-09-27 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0004_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address1',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address2',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='city',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='email',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='name',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='state',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='zip_code',
        ),
    ]