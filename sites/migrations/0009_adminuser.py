# Generated by Django 4.0.3 on 2022-04-11 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0008_alter_appusername_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]
