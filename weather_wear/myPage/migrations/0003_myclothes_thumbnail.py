# Generated by Django 3.2.5 on 2021-07-03 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPage', '0002_myclothes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='myclothes',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]