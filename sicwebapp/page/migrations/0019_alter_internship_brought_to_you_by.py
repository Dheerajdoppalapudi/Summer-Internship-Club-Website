# Generated by Django 4.0 on 2022-05-30 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0018_internship_brought_to_you_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internship',
            name='brought_to_you_by',
            field=models.CharField(blank=True, choices=[('Student Internship Club', 'Student Internship Club'), ('GCGC', 'GCGC'), ('CGC Visakhapatnam', 'CGC Visakhapatnam'), ('CGC Hyderabad', 'CGC Hyderabad'), ('CGC Bengaluru', 'CGC Bengaluru')], default='Student Internship Club', max_length=70),
        ),
    ]
