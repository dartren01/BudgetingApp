# Generated by Django 2.2.12 on 2020-05-28 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='current_monthly_goal',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
