# Generated by Django 2.1.4 on 2018-12-31 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0004_auto_20181231_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='code_answer',
            name='qestion_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
