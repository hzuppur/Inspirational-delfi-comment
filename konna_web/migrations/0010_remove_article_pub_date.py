# Generated by Django 3.0.6 on 2020-05-17 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('konna_web', '0009_article_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='pub_date',
        ),
    ]
