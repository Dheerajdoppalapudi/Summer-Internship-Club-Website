# Generated by Django 4.0 on 2022-12-16 13:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('page', '0023_remove_scolarships_branch_scolarships_multibranch'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='registered',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
