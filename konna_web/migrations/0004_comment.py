# Generated by Django 3.0.6 on 2020-05-16 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('konna_web', '0003_auto_20200516_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000)),
                ('subject', models.CharField(max_length=100)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='konna_web.Article')),
            ],
        ),
    ]
