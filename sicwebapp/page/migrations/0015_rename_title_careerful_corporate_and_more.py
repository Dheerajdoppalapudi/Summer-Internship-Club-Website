# Generated by Django 4.0 on 2022-05-30 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0014_rename_package_careerful_package'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careerful',
            old_name='title',
            new_name='corporate',
        ),
        migrations.RemoveField(
            model_name='careerful',
            name='comapny_org',
        ),
    ]