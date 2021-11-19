# Generated by Django 3.2.8 on 2021-11-08 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='body',
        ),
        migrations.AddField(
            model_name='goal',
            name='custom_goal',
            field=models.CharField(default='I want to follow this program for 1 month.', max_length=250),
        ),
        migrations.AddField(
            model_name='goal',
            name='selected_goal',
            field=models.CharField(default='I want to increase my endurance', max_length=100),
        ),
    ]