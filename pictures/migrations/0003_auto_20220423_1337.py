# Generated by Django 2.2.6 on 2022-04-23 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_picture_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]