# Generated by Django 2.2.3 on 2019-07-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_loginkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='privacypolicy',
            name='cached_score',
            field=models.FloatField(default=None, null=True),
        ),
    ]