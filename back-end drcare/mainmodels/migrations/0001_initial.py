# Generated by Django 3.2.12 on 2022-05-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=200)),
                ('imagefile', models.FileField(upload_to='C:\\Users\\Un-Known\\Desktop\\Final Final Project\\API\\GradProjectAPI\\API\\gradprojectapi\\mainmodels\\models\\leukemia\\leukemiaImages')),
            ],
        ),
    ]
