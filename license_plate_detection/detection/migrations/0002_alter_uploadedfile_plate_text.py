# Generated by Django 5.0.6 on 2024-07-14 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='plate_text',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]