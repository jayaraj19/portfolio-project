# Generated by Django 2.0.6 on 2018-08-18 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20180818_1004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='image',
            new_name='img',
        ),
    ]