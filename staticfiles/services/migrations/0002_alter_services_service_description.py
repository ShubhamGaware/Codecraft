# Generated by Django 5.0.3 on 2024-04-14 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_description',
            field=models.CharField(max_length=100),
        ),
    ]