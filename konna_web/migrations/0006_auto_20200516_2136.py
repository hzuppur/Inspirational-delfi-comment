# Generated by Django 3.0.6 on 2020-05-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('konna_web', '0005_commentreply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='subject',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='commentreply',
            name='subject',
            field=models.CharField(max_length=500),
        ),
    ]
