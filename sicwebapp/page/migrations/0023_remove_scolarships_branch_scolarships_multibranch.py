# Generated by Django 4.0 on 2022-07-20 08:59

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0022_alter_careerful_package'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scolarships',
            name='branch',
        ),
        migrations.AddField(
            model_name='scolarships',
            name='multibranch',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Engineering', 'Engineering'), ('Management', 'Management'), ('Medical and Paramedical', 'Medical and Paramedical'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Law', 'Law'), ('Sciences', 'Sciences'), ('Pharmacy', 'Pharmacy'), ('Nursing', 'Nursing'), ('Everyone', 'Everyone')], default='Everyone', max_length=116),
        ),
    ]