# Generated by Django 2.1.4 on 2019-04-19 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0014_ghresult_lastversions_repo_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='GHResult_KeywordMeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.IntegerField()),
                ('ghUrl', models.CharField(max_length=1000)),
                ('repo_name', models.CharField(blank=True, default='', max_length=300)),
                ('is_vulnerable', models.BooleanField(default=False, verbose_name='Vulnerable ?')),
                ('is_checked', models.BooleanField(default=False, verbose_name='Checked ?')),
                ('is_error', models.BooleanField(default=False, verbose_name='ERROR ?')),
                ('report', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='panel.Code')),
            ],
            options={
                'verbose_name_plural': 'Github Results - Keyword Meter',
            },
        ),
        migrations.AlterUniqueTogether(
            name='ghresult_keywordmeter',
            unique_together={('answer_id', 'ghUrl', 'code')},
        ),
    ]
