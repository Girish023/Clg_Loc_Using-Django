# Generated by Django 5.1.1 on 2024-09-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangovarity',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
