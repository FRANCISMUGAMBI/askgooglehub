# Generated by Django 4.0.4 on 2022-05-06 08:22

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_category', models.CharField(choices=[('TEC', 'Technical'), ('PRO', 'Programming'), ('HOW', 'HOW TO'), ('OTH', 'Other')], max_length=3)),
                ('title', models.CharField(max_length=150, verbose_name='Page Title')),
                ('url_name', models.CharField(max_length=40, validators=[articles.models.validate_name], verbose_name='Url Name')),
                ('photo', models.ImageField(upload_to='photos')),
                ('paragrah1', models.TextField(verbose_name='Paragraph1')),
                ('header2', models.CharField(max_length=150, verbose_name='Header2 (optional)')),
                ('paragrah2', models.TextField(verbose_name='Paragraph2')),
                ('header3', models.CharField(max_length=150, verbose_name='Header3 (optional)')),
                ('paragrah3', models.TextField(verbose_name='Paragraph3')),
                ('header4', models.CharField(max_length=150, verbose_name='Header4 (optional)')),
                ('paragrah4', models.TextField(verbose_name='Paragraph4')),
                ('header5', models.CharField(max_length=150, verbose_name='Header5 (optional)')),
                ('paragrah5', models.TextField(verbose_name='Paragraph5')),
                ('release_date', models.DateField()),
            ],
        ),
    ]
