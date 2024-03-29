# Generated by Django 4.0 on 2022-04-07 16:09

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_alter_certifications_date_posted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='internship',
            name='multibranch',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Engineering', 'Engineering'), ('Management', 'Management'), ('Medical and Para-medical', 'Medical and Para-medical'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Law', 'Law'), ('Sciences', 'Sciences'), ('Pharmacy', 'Pharmacy'), ('Nursing', 'Nursing')], max_length=108),
        ),
    ]
