# Generated by Django 3.2.13 on 2022-07-03 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmodels', '0003_rename_image_image_imagefiled'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imageUrl',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
