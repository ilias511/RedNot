# Generated by Django 4.0.3 on 2022-04-04 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0003_alter_post_title_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.URLField(),
        ),
    ]