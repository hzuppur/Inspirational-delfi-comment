# Generated by Django 3.0.6 on 2020-05-16 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konna_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_id',
            field=models.IntegerField(default=42),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='href',
            field=models.CharField(default=42, max_length=500),
            preserve_default=False,
        ),
    ]
