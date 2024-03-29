# Generated by Django 4.0 on 2022-04-08 15:27

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0009_remove_internship_multibranch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='internship',
            name='branch',
        ),
        migrations.AddField(
            model_name='internship',
            name='multibranch',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Engineering', 'Engineering'), ('Management', 'Management'), ('Medical and Para-medical', 'Medical and Para-medical'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Law', 'Law'), ('Sciences', 'Sciences'), ('Pharmacy', 'Pharmacy'), ('Nursing', 'Nursing'), ('Everyone', 'Everyone')], default='Everyone', max_length=117),
        ),
        migrations.AlterField(
            model_name='scolarships',
            name='branch',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Management', 'Management'), ('Medical and Para-medical', 'Medical and Para-medical'), ('Humanities and Social Sciences', 'Humanities and Social Sciences'), ('Law', 'Law'), ('Sciences', 'Sciences'), ('Pharmacy', 'Pharmacy'), ('Nursing', 'Nursing'), ('Everyone', 'Everyone')], default='Everyone', max_length=50),
        ),
    ]
