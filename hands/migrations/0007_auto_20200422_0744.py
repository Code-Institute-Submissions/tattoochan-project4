# Generated by Django 2.0.2 on 2020-04-22 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hands', '0006_auto_20200422_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hands_info',
            name='portrait',
            field=models.ImageField(default='images/default_pic.png', null=True, upload_to='images/'),
        ),
    ]
