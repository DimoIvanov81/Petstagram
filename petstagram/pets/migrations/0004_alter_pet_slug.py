# Generated by Django 5.1.3 on 2024-11-08 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pet_date_of_birth_pet_name_pet_personal_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
