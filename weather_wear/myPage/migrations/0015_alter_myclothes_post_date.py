# Generated by Django 3.2.5 on 2021-07-14 14:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myPage', '0014_alter_myclothes_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclothes',
            name='post_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]