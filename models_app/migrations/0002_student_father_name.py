# Generated by Django 5.0 on 2023-12-27 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.TextField(default='rahim'),
        ),
    ]
