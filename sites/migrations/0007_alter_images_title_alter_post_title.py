# Generated by Django 4.0.3 on 2022-04-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0006_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='title',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]