# Generated by Django 4.0.3 on 2022-04-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Sport', 'Sport'), ('Politics', 'Politics'), ('Article', 'Article'), ('Fun Fact', 'Fun Fact'), ('International News', 'International News'), ('Joke', 'Joke'), ('Crypto', 'Crypto'), ('Gaming', 'Gaming'), ('Movies', 'Movies'), ('Other', 'Other')], max_length=100),
        ),
    ]