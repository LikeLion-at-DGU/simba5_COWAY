# Generated by Django 4.2.2 on 2023-06-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_post_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='image',
            field=models.ImageField(blank=True, upload_to='info/'),
        ),
    ]
