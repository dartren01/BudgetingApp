# Generated by Django 3.0.4 on 2020-05-08 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgeting', '0004_auto_20200507_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='source',
            field=models.CharField(max_length=30, verbose_name='Source (Case Sensitive)'),
        ),
    ]