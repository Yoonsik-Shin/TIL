# Generated by Django 3.2.13 on 2022-10-20 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='content',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]
