# Generated by Django 4.2.20 on 2025-04-26 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0012_faculty_sl_alter_faculty_designation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='citation',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
