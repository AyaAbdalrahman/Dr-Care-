# Generated by Django 3.2.13 on 2022-07-03 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmodels', '0005_remove_image_imageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='namefiled',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]