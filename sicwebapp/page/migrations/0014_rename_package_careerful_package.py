# Generated by Django 4.0 on 2022-05-22 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0013_careerful'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careerful',
            old_name='Package',
            new_name='package',
        ),
    ]